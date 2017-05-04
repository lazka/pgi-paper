Introduction
------------

Looking at the various different Python interpreter implementations PyPy
stands out as one of the most complete and compatible with CPython while
providing significant performance improvements for certain workloads. For a
subset of benchmarks PyPy uses to track its performance over time it performs
over 7 times faster than CPython 2 (see http://speed.pypy.org/). Compared to
other implementations like Jython or IronPython it is more feature complete in
regards to the language features and the standard library, as for example it
is the only implementation containing a fully functional "ctypes" module for
interacting with shared libraries. In some case PyPy even acts as a testing
ground for new features of CPython. A proposed new dict (Python's hash table)
implementation proposed by a Python developer (see
https://mail.python.org/pipermail/python-dev/2012-December/123028.html) was
first tested in PyPy (see https://bugs.python.org/issue27350)

While PyPy has various advantages, in practice it is not the implementation of
choice for many applications. Some reasons being the worse startup
performance, the unpredictability of performance due to the JIT and the used
garbage collector strategy or the increased initial memory usage. One reason
more is its lack of support for CPython C extensions, which provide Python
interfaces for C libraries and are written in C against the public C API of
CPython. One of those libraries, commonly used under Linux, is PyGObject,
which provides a Python interface for libraries build on the GObject object
system. One such library for example is GTK+, a cross platform GUI toolkit.

This paper looks at the various possibilities in how to create an PyGObject
alternative which works with both CPython and Pypy, and for any implementation
which does not provide full CPython C API support. We think that having a
working alternative to PyGObject would help PyPy get wider usage as it
currently lacks bindings for a cross platform GUI toolkit. But PyGObject not
only provides access to GTK+, but also many other useful libraries such as
glib, GStreamer and WebKitGTK.
