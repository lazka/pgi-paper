#!/bin/bash
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

set -e

DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$DIR"

source ../venv_tools.sh;

setup_pypy;

setup_cpython_env;
python main.py python bench-cffilib.py
python main.py python bench-clib.py
remove_cpython_env;

setup_pypy_env;
python main.py python bench-cffilib.py
python main.py python bench-clib.py
python main.py python --jit off bench-cffilib.py
python main.py python --jit off bench-clib.py
remove_pypy_env;

remove_pypy;
