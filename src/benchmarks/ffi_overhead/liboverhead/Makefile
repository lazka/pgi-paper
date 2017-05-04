# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

NAME=overhead

all: $(NAME).so

$(NAME).so: $(NAME).o
	libtool --mode=link gcc --shared $(NAME).c -o lib$(NAME).so

$(NAME).o: $(NAME).c $(NAME).h
	libtool --mode=compile gcc --shared $(NAME).c

.PHONY: clean
 
clean:
	rm -f $(NAME).o $(NAME).lo lib$(NAME).so
