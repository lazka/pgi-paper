#!/usr/bin/python
# Copyright 2015 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

import subprocess
import sys
sys.path.insert(0, "..")
from benchutils import *


def main(argv):
    print argv[-1], subprocess.check_output(argv[1:-1] + ["info.py"])
    values = []
    for i in xrange(1000):
        data = subprocess.check_output(argv[1:]).strip()
        values.append(float(data))
    print average(values), stdev(values)


if __name__ == "__main__":
    main(sys.argv)
