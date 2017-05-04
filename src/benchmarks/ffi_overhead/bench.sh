#!/bin/bash
#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

export LD_LIBRARY_PATH=liboverhead
echo "python cffi"
python bench_overhead.py
echo "python capi"
python bench_overhead.py capi
echo "pypy cffi"
pypy bench_overhead.py
echo "pypy cffi nojit"
pypy --jit off bench_overhead.py
echo "pypy capi"
pypy bench_overhead.py capi
