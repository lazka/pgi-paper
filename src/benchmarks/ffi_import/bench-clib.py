#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

import sys
import os
sys.path.insert(0, "..")
from benchutils import *

from distutils.sysconfig import get_python_lib
pgi_path = os.path.join(get_python_lib(), "pgi")
sys.path.insert(0, pgi_path)

t = timer()
import clib.gir
print timer() - t
