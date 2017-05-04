# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

all: libnoop.so

libnoop.so: noop.o
	libtool --mode=link gcc -O2 --shared noop.c -o libnoop.so

noop.o: noop.c noop.h
	libtool --mode=compile gcc -O2 --shared noop.c

.PHONY: clean
 
clean:
	rm -f noop.o noop.lo libnoop.so
