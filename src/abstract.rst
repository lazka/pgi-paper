Abstract
========

The scripting language Python has many successful applications as a glue
language, bringing together low-level libraries in a scripting environment. In
the past few years multiple alternative Python interpreter implementations
like PyPy, IronPython and Jython have surfaced which focus on performance or
improving integration with other language ecosystems. All of them suffer under
the wide usage of Python extensions using the CPython C API, which is hard or
impossible to implement for other VMs because it exposes many of the CPython
implementation details such as reference counting. The resulting lack of
usable extensions does not make these VMs a viable alternative for many
applications and prevents their wider usage. This paper focuses on the PyPy
interpreter and the CPython extension PyGObject, which provides Python
interfaces for libraries based on the GObject system such as GTK+, GLib and
GStreamer. PyGObject is widely used for application development for the GNOME
desktop environment but also for cross platform applications and as GUI
back-end for visualization libraries such as matplotlib. This paper covers how
an alternative implementation of PyGObject, which also supports PyPy, would
look like and how it compares the PyGObject. Further more this paper addresses
the current lack of complete and sound documentation of the by PyGObject
exposed API.

To help with various design decisions for an alternative PyGObject
implementation this paper evaluates various approaches for interfacing with C
libraries from PyPy and compares them with CPython. Based on these evaluations
a prototype implementation called PGI is presented. PGI is compatible with
PyGObject and produces bindings at runtime by generating Python code that uses
ctypes/cffi to interface with the GObject based libraries. Based on this
prototype implementation a documentation generator is presented which
interfaces with the PGI extension to produce complete and sound API
documentation for the generated interfaces. Since PGI is compatible with
PyGObject the documentation is valid for both implementations.

While the prototype implementation is far from feature complete, the
documentation generation it enables is now the default source of documentation
for PyGObject users. The generated documentation helps users of PyGObject and
PGI alike and reduces the initial hurdle for new users, especially those not
familiar with C. Further more the presented evaluation of binding techniques
can be helpful for similar projects, trying to provide performant bindings for
PyPy.
