import time
import cffi
import math
import sys

sys.path.insert(0, "..")
from benchutils import average, stdev, timer


def create_function():
    """Creates a new cfi function, which calls the library one"""

    ffi = cffi.FFI()
    ffi.cdef("""
int overhead(int32_t* list, size_t num, char* utf8, int* error);
""")
    c = ffi.dlopen("./liboverhead/liboverhead.so")
    overhead = c.overhead

    def func(list_, length, text, error):
        return overhead(list_, length, text, error)

    return overhead


def create_checked_function():
    """Creates a new cfi function, which calls the library one"""

    ffi = cffi.FFI()
    ffi.cdef("""
int overhead(int32_t* list, size_t num, char* utf8, int* error);
""")
    c = ffi.dlopen("./liboverhead/liboverhead.so")
    overhead = c.overhead

    error_type = ffi.typeof("int*")

    def func(list_, text):
        # typecheck/convert text
        if isinstance(text, unicode):
            text = text.encode("utf-8")
        elif text is None:
            text = ffi.NULL
        elif not isinstance(text, str):
            raise TypeError

        len_ = len(list_)
        error = ffi.new(error_type)
        result = overhead(list_, len_, text, error)

        if not result:
            raise Exception("Error occured: %d" % error[0])

        return result

    return func


def benchmark_function(func, *args):
    r = []
    for i in xrange(3000):
        t = timer()
        for i in xrange(5000):
            func(*args)
        r.append(timer() - t)
    return "%.5f" % (average(r) * 1000), "%.5f" % (stdev(r) * 1000)


def test_function(func):
    """Verify value and type checking of the wrapped cffi function.

    There should not be overflows, crashes etc.
    """

    def assertRaises(exc, func, *args):
        try:
            func(*args)
        except exc:
            pass
        else:
            raise Exception("%r not raised" % exc)


    class Number(object):
        def __init__(self, value):
            self.value = value

        def __int__(self):
            return self.value

    assertRaises(OverflowError, func, [0, 2**34], "")
    assertRaises(OverflowError, func, [2**34], "")
    assertRaises(OverflowError, func, [Number(2**34)], "")
    assertRaises(TypeError, func, [], 1)
    assertRaises(TypeError, func, None, "")
    func([1, 2, 3], "")
    func([1, 2, 2**31-1], "")
    func([1, 2, 3], u"hello")
    func([1, 2, Number(42)], "")
    func([1, 2, Number(42)], None)


def main():
    if "capi" in sys.argv:
        from cwrapper import cwrapper
        wrapped = cwrapper.overhead
        test_function(wrapped)

        # warmup
        benchmark_function(wrapped, [1, 2, 3, 4], u"foobar")
        print "wrapped", benchmark_function(wrapped, [1, 2, 3, 4], u"foobar")
        return

    func = create_function()
    wrapped = create_checked_function()

    # verify that the wrapper fulfills all requirements
    test_function(wrapped)

    # warmup
    benchmark_function(wrapped, [1, 2, 3, 4], u"foobar")
    print "wrapped", benchmark_function(wrapped, [1, 2, 3, 4], u"foobar")

    ffi = cffi.FFI()
    benchmark_function(func, [1, 2, 3, 4], 4, b"foobar", ffi.NULL)
    print "bare", benchmark_function(func, [1, 2, 3, 4], 4, b"foobar", ffi.NULL)


if __name__ == "__main__":
    main()
