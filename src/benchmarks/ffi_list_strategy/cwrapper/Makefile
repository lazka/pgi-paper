# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

all: cwrapper.so

cwrapper.so: cwrapper.c
	python ./setup.py build --build-platlib .
	python ./setup.py clean

.PHONY: clean

clean:
	rm -rf cwrapper.so build
