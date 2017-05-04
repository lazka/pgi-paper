#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

"""
Showcase for resource handling in combination with the garbage collector

1) Create an external resource
2) Remove all Python references to it and wait
3) Measure memory usage along the way
"""

from __future__ import print_function

import gc
import os
import sys
import time
import ctypes
import threading
import platform


lib = ctypes.CDLL('libc.so.6')
malloc = lib.malloc
malloc.argtypes = [ctypes.c_size_t]
malloc.restype = ctypes.c_void_p

memset = lib.memset
memset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t]
memset.restye = ctypes.c_void_p

free = lib.free
free.argtypes = [ctypes.c_void_p]
free.restype = ctypes.c_void_p


def get_memory_usage(pid):
    """Returns the RSS of the current process

    Args:
        pid (int): process ID
    Returns:
        int
    """

    with open("/proc/%d/smaps" % pid, "rb") as h:
        sum_ = 0
        for line in h.read().decode("utf-8").splitlines():
            if line.startswith("Rss:"):
                sum_ += int(line.split()[1]) * 1024
        return sum_


def add_memory_pressure(num_bytes):
    """Adds memory pressure if supported by the interpreter

    Args:
        num_bytes (int): either positiv to add pressure or negative to remove

    """

    try:
        import __pypy__
    except ImportError:
        pass
    else:
        __pypy__.add_memory_pressure(num_bytes)


class Resource(object):
    """An object which allocates some memory using the system allocator.
    In case this object gets finalized the memory will be freed
    """

    def __init__(self, num_bytes, pressure=False):
        """
        Args:
            num_bytes (int): number of bytes to allocate
            pressure (bool): if memory pressure should be added if possible
        """

        res = malloc(num_bytes)
        assert res
        # memset to make sure things get allocated
        memset(res, 42, num_bytes)
        self._res = res
        self._pressure = 0

        if pressure:
            add_memory_pressure(num_bytes)
            self._pressure = num_bytes

    def __del__(self):
        free(self._res)
        if self._pressure:
            add_memory_pressure(-self._pressure)


def main(argv):
    assert len(argv) == 2

    t = time.time()
    name = argv[1]

    res = os.fork()
    if res == 0:
        # child
        # create the resource, wait a bit, remove references, wait a bit more
        time.sleep(0.5)
        resources = []
        for i in range(25):
            r = Resource(2 ** 25, "pressure" in argv[1])
            time.sleep(0.05)
            del r
        gc.collect()
        time.sleep(4)
    else:
        total = 3
        N = 200
        for i in range(N):
            print(name, "%07.4f" % (time.time() - t), get_memory_usage(res))
            time.sleep(total / float(N))
        os.waitpid(res, 0)


if __name__ == "__main__":
    main(sys.argv)
