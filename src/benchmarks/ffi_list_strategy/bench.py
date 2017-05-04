#!/usr/bin/python
# Copyright 2015 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

"""
Passes an array of 1000 int to a C function, using cffi or the CPython C API
"""

import sys
import time
import math


def average(r):
    return float(sum(r)) / len(r)


def variance(r):
    avg = average(r)
    return float(sum(map(lambda x: (x - avg) ** 2, r))) / (len(r) - 1)


def stdev(r):
    return math.sqrt(variance(r))


def check_error_handling(func):
    """This makes sure the wrapper function handles invalid input.

    Raises AssertionError in case the wrapper doesn't do so.
    """

    func([])
    func(tuple())

    try:
        func([2**50])
    except OverflowError:
        pass
    else:
        raise AssertionError("missing overflow error")

    try:
        func([object()])
    except TypeError as e:
        pass
    else:
        raise AssertionError("missing type error")


def run(func, rounds=1000, taint=False):
    """taint will add a object to the list and remove it again; this will
    switch the storage strategy the passed list for PyPy from int to object.
    """

    l = list(range(1000))

    if taint:
        l.append(object())
        l.pop(-1)

    try:
        import __pypy__
    except ImportError:
        pass
    else:
        print __pypy__.strategy(l)

    results = []
    for i in xrange(rounds):
        t = time.time()
        for i in xrange(1000):
            func(l)
        results.append(time.time() - t)
    return results


def main(mode):

    if mode == "cpython-capi":
        from cwrapper.cwrapper import int_list_args

        func = int_list_args

    else:
        import cffi
        ffi = cffi.FFI()
        ffi.cdef("void int_list_args(int* list);")
        c = ffi.dlopen("libnoop.so")
        int_list_args = c.int_list_args

        def func(l):
            int_list_args(ffi.new("int[]", l))

    check_error_handling(func)
    run(func, 1000)
    res = run(func, 1000)
    print "----", mode
    print "norm ", average(res) * 1000, stdev(res) * 1000
    res = run(func, 1000, taint=True)
    print "taint", average(res) * 1000, stdev(res) * 1000


if __name__ == "__main__":
    modes = ["pypy-cffi", "cpython-cffi", "cpython-capi"]
    mode = sys.argv[1]
    assert mode in modes
    main(mode)
