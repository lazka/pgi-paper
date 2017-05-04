#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

DIRS = libnoop cwrapper

all:
	for d in $(DIRS); do (cd $$d; $(MAKE)); done

clean:
	for d in $(DIRS); do (cd $$d; $(MAKE) clean); done

.PHONY: clean
