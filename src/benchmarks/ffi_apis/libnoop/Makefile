all: libnoop.so

libnoop.so: noop.o
	libtool --mode=link gcc -O2 --shared noop.c -o libnoop.so

noop.o: noop.c noop.h
	libtool --mode=compile gcc -O2 --shared noop.c

.PHONY: clean
 
clean:
	rm -f noop.o noop.lo libnoop.so
