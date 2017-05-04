#!/bin/sh
#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

make clean
make
export LD_LIBRARY_PATH=libnoop

pypy ./bench.py pypy-cffi
pypy --jit off ./bench.py pypy-cffi
python ./bench.py cpython-cffi
python ./bench.py cpython-capi
