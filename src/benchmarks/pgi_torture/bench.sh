#!/bin/bash

make

export LD_LIBRARY_PATH=.
export GI_TYPELIB_PATH=.
export PYTHONPATH=/home/lazka/Desktop/pgi

python main.py
python main.py pgi
pypy main.py pgi
