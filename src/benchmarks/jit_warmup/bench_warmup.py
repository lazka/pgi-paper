#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

import pypyjit
pypyjit.set_param("off")

# reduce variance
import gc
gc.disable()

import ctypes
import time

N = 70

def with_jit():
    pypyjit.set_param("default")

    libc = ctypes.CDLL("libc.so.6")
    strlen = libc.strlen
    strlen.argtypes = [ctypes.c_char_p]
    strlen.restype =  ctypes.c_size_t

    result = []
    for i in xrange(N):
        t = time.time()
        for j in xrange(100):
            strlen("foobar")
        result.append(time.time() - t)
    return result


def without_jit():
    pypyjit.set_param("off")

    libc = ctypes.CDLL("libc.so.6")
    strlen = libc.strlen
    strlen.argtypes = [ctypes.c_char_p]
    strlen.restype =  ctypes.c_size_t

    result = []
    for i in xrange(N):
        t = time.time()
        for j in xrange(100):
            strlen("foobar")
        result.append(time.time() - t)
    return result


if __name__ == "__main__":
    print " ".join(map(str, without_jit()))
    print " ".join(map(str, with_jit()))
