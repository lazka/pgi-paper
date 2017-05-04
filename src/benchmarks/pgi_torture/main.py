#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.


import sys
import platform
sys.path.insert(0, "..")
from benchutils import *


def benchmark_function(func, *args):
    r = []
    for i in xrange(3000):
        t = timer()
        for i in xrange(1000):
            func(*args)
        r.append(timer() - t)
    return "%.5f" % (average(r) * 1000), "%.5f" % (stdev(r) * 1000)


def main(argv):
    use_pgi = "pgi" in argv[1:]
    if use_pgi:
        import pgi
        pgi.install_as_gi()

    import gi
    gi.require_version("Regress", "1.0")
    from gi.repository import Regress

    object_ = Regress.TestObj()

    print platform.python_implementation(), "pgi" if use_pgi else "gi",
    benchmark_function(object_.torture_signature_0, 5000, "Torture Test 1", 12345)
    benchmark_function(object_.torture_signature_0, 5000, "Torture Test 1", 12345)
    print benchmark_function(object_.torture_signature_0, 5000, "Torture Test 1", 12345)


if __name__ == "__main__":
    main(sys.argv)
