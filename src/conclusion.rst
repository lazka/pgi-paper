Conclusion and Future Work
==========================

This paper presented a range of benchmarks comparing different ways to access
shared libraries in Python with both CPython and PyPy and showed that
performance wise PyPy & cffi can compete with C extensions written for CPython
even if value validation and error handling is implemented in Python.

Based on these insights, a PyGObject compatible library, PGI, was implemented
and presented which runs under both CPython and PyPy using the ctypes and cffi
modules. In its current state PGI is only able to run smaller example programs
and no real world applications. Further more PGI-Docgen was presented which
generates complete and sound documentation based on PGI and GObject
Introspection which is also helpful to existing users of PyGObject.

During the work on PGI and PGI-Docgen it became clear that PyGObject is
lacking maintainership for the implementation and the surrounding
documentation. Thus any work done in that area should be focused on PyGObject
itself and not on PGI or other alternatives, since the prevalence of PGI also
depends on the prevalence of PyGObject. The author of this paper has thus
`started to contribute
<https://git.gnome.org/browse/pygobject/log/?qt=author&q=Christoph+Reiter>`__
to PyGObject instead of pursuing further improvements of PGI for the time
being.


External Resources
==================

These resources where created as part of this project and contain more
information about their respective application or library:

The bechmarking code used for the presented results and plots:
    https://bitbucket.org/lazka/pypy-gi-bench

The GIT repository of the PGI library:
    https://github.com/lazka/pgi

The GIT repository of the PGI-Docgen program:
    https://github.com/lazka/pgi-docgen

The online version of the documentation generated with PGI-Docgen:
    https://lazka.github.io/pgi-docs/

The GIT repository of PGI-Docgen generated Devhelp packages:
    https://github.com/pygobject/pgi-docs-devhelp

The PYPUI example framework:
    https://github.com/lazka/pypui
