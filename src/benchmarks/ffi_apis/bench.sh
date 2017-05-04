#!/bin/bash

set -e

DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$DIR"

source ../venv_tools.sh;

setup_pypy;

# build everything
make clean
make
export LD_LIBRARY_PATH=libnoop

# clear result file
RESULT=result.temp
echo "" > "$RESULT"

# run CPython benchmarks
setup_cpython_env;

python --version
pip install --upgrade pycparser=="$PYCPARSER_VERSION"
pip install --upgrade cffi=="$CFFI_VERSION"
python main.py >> "$RESULT"

remove_cpython_env;


# run PyPy benchmarks
setup_pypy_env;

python --version
pip install --upgrade pycparser=="$PYCPARSER_VERSION"
pip install --upgrade cffi=="$CFFI_VERSION"
pypy main.py >> "$RESULT"
pypy --jit off main.py nojit >> "$RESULT"

remove_pypy_env;

# remove pypy
remove_pypy;

# plot results
cat "$RESULT" | ./plot_bench.py
rm "$RESULT"
make clean
