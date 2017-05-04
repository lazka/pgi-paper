#!/bin/bash

set -e

PYPY_VERSION="5.6"
CFFI_VERSION="1.9.1"
PYCPARSER_VERSION="2.17"
PGI_VERSION="0.0.11.1"

function setup_pypy {
    # get pypy
    PYPY_DIR="pypy-$PYPY_VERSION-linux_x86_64-portable"

    if [ ! -d "$PYPY_DIR" ]; then
        wget -c "https://bitbucket.org/squeaky/portable-pypy/downloads/$PYPY_DIR.tar.bz2"
        tar xvjf "$PYPY_DIR.tar.bz2"
        rm "$PYPY_DIR.tar.bz2"
    fi

    OLD_PATH=$PATH
    export PATH="$(pwd)/$PYPY_DIR/bin":$PATH
}

function remove_pypy {
    export PATH=$OLD_PATH
    rm -Rf "$PYPY_DIR"
}

function install_deps {
    pip install --upgrade pycparser=="$PYCPARSER_VERSION"
    pip install --upgrade cffi=="$CFFI_VERSION"
    pip install --upgrade pgi=="$PGI_VERSION"
}

function setup_pypy_env {
    rm -Rf venv_pypy
    virtualenv-pypy --no-site-packages --python=pypy venv_pypy
    source venv_pypy/bin/activate
    install_deps
}

function remove_pypy_env {
    deactivate
    rm -Rf venv_pypy
}

function setup_cpython_env {
    rm -Rf venv_python
    virtualenv --no-site-packages --python=python venv_python
    source venv_python/bin/activate
    install_deps
}

function remove_cpython_env {
    deactivate
    rm -Rf venv_python
}
