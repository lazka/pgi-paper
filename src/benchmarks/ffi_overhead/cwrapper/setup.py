#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

from distutils.core import setup, Extension

setup(
    name='cwrapper',
    version='1.0',
    ext_modules=[
        Extension(
            'cwrapper',
            sources=['cwrapper.c'],
            include_dirs=['../liboverhead'],
            library_dirs=['../liboverhead'],
            libraries=["overhead"]),
    ],
)
