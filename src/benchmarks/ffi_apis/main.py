#!/usr/bin/python
# Copyright 2014 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

import sys
import math
import timeit
import platform
sys.path.insert(0, "..")
from benchutils import *


ROUNDS = 3000
LOOP = 1000
WARMUP_ROUNDS = 3000
IMPLE_SUBFIX = "-nojit" if "nojit" in sys.argv else ""


def time_function(func, args, desc, rounds=ROUNDS, warmup=WARMUP_ROUNDS):
    global timer

    name = func.__name__
    impl = platform.python_implementation() + IMPLE_SUBFIX
    timer = timer

    # test ROUNDS rounds and return the best
    results = []
    for i in xrange(rounds + warmup):
        t = timer()
        func(*args)
        results.append(timer() - t)

    results = results[warmup:]
    assert len(results) == rounds

    print "%-10s %-10s %-15s %.15f %.15f" % (
        impl, desc, name, average(results), stdev(results))


def bench_void(func, loop=LOOP):
    for i in xrange(loop):
        func()


def bench_str(func, loop=LOOP):
    for i in xrange(loop):
        func("foobar")


def bench_double(func, loop=LOOP):
    for i in xrange(loop):
        func(42.42)


def main(argv):
    #####################################################

    import threading
    threading.Thread(target=lambda: None).start()

    print >> sys.stderr, \
        "Each called %d times, avg of %d runs" % (LOOP, ROUNDS)

    ### C-API ###########################################

    from cwrapper import cwrapper
    time_function(bench_void, [cwrapper.noop_void], "C-API")
    time_function(bench_str, [cwrapper.noop_str], "C-API")
    time_function(bench_double, [cwrapper.noop_double], "C-API")

    ### CTYPES ###########################################

    import ctypes
    libnoop = ctypes.CDLL("./libnoop/libnoop.so")

    noop_str = libnoop.noop_str
    noop_str.argtypes = [ctypes.c_char_p]
    noop_str.restype =  ctypes.c_size_t

    noop_double = libnoop.noop_double
    noop_double.argtypes = [ctypes.c_double]
    noop_double.restype = ctypes.c_double

    noop_void = libnoop.noop_void
    noop_void.argtypes = []
    noop_void.restype = None

    time_function(bench_void, [noop_void], "ctypes")
    time_function(bench_str, [noop_str], "ctypes")
    time_function(bench_double, [noop_double], "ctypes")

    ### CFFI ###########################################

    import cffi

    ffi = cffi.FFI()
    ffi.cdef("""
    void noop_void(void);
    double noop_double(double);
    size_t noop_str(char*);
    """)

    c = ffi.dlopen("./libnoop/libnoop.so")
    noop_void = c.noop_void
    noop_double = c.noop_double
    noop_str = c.noop_str

    time_function(bench_void, [noop_void], "cffi")
    time_function(bench_str, [noop_str], "cffi")
    time_function(bench_double, [noop_double], "cffi")


if __name__ == "__main__":
    main(sys.argv)
