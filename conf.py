# -*- coding: utf-8 -*-

import sys, os

source_suffix = '.rst'
master_doc = 'src/index'
project = u'Runtime Generated GObject Introspection Bindings for PyPy'
copyright = u'2016, Christoph Reiter'
version = '1.0'
release = '1.0'
exclude_patterns = ['_html', '_latex']
pygments_style = 'tango'
#html_theme = 'sphinx_rtd_theme'
numfig = True

html_show_copyright = False

html_context = {
    'extra_css_files': [
        '_static/extra.css',
    ],
}

html_static_path = [
    "extra.css",
]
