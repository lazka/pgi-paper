Related Work
============

There exist two unfinished projects with a similar goal, to bring GObject
library support to PyPy:

First a `fork <https://github.com/jdahlin/pygobject>`__ of PyGObject that
partially implements the PyGObject API with ctypes. While this 1:1 translation
from C code to ctypes would probably need less work to get 100% compatibility
with PyGObject, the C code is designed around the idea that calls to shared
libraries are cheap. This is not the case if ctypes is used and would lead to
bad performance compared to PyGObject. The fork is currently unmaintained.

Secondly, the project `pygir-ctypes
<http://code.google.com/p/pygir-ctypes/>`__ exists with the goal to implement
bindings for PyPy/CPython2.x/3.x that are not compatible with PyGObject. It
does run minimal examples in its current form, but has shortcomings as it does
not free any memory it allocates and the code is hard to extend. The project
is also inactive.

Related to the goal of providing PyPy support for a GUI toolkit `wxpython_cffi
<https://bitbucket.org/waedt/wxpython_cffi>`__ tries to implement a wxPython
compatible interface. The project, which was part of `Google Summer of Code
<https://developers.google.com/open-source/gsoc/>`__, is no longer maintained
and past implementation status reports can be found in the `project associated
blog <http://waedt.blogspot.co.at/>`__.
