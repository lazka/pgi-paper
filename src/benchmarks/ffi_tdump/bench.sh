#!/bin/bash
set -e

DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$DIR"

rm -Rf venv_pypy
rm -Rf venv_cpython

# pypy

virtualenv --python=pypy venv_pypy
source venv_pypy/bin/activate
pip install cffi==0.9.2
pip install pgi==0.0.10.1
echo "pypy cffi"
python tdump_bench.py cffi
echo "pypy ctypes"
python tdump_bench.py ctypes

deactivate

# cpython

virtualenv --python=pypy venv_cpython
source venv_cpython/bin/activate
pip install cffi==0.9.2
pip install pgi==0.0.10.1

echo "cpython cffi"
python tdump_bench.py cffi
echo "cpython ctypes"
python tdump_bench.py ctypes

# cleanup

rm -Rf venv_pypy
rm -Rf venv_cpython
