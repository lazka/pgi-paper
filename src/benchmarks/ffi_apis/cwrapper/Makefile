PYPY_SUFFIX=$(shell pypy -c 'import imp; print imp.get_suffixes()[0][0],')

all: cwrapper.so cwrapper$(PYPY_SUFFIX)

cwrapper.so: cwrapper.c
	python ./setup.py build --build-platlib .
	python ./setup.py clean

cwrapper$(PYPY_SUFFIX): cwrapper.c
	pypy --version
	pypy ./setup.py build --build-platlib .
	pypy ./setup.py clean

.PHONY: clean

clean:
	rm -rf cwrapper*.so build
