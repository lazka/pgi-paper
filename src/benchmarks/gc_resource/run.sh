#!/bin/bash
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

rm -f data.txt
pypy gc_resource.py "PyPy" >> data.txt
pypy gc_resource.py "PyPy-pressure" >> data.txt
python2 gc_resource.py "CPython-2" >> data.txt
python3 gc_resource.py "CPython-3" >> data.txt
cat data.txt | python plot.py
rm data.txt
