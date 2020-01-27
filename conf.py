# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Kaleide School Docs'
copyright = '2020, Diana Isabel de Horna Cicka, Diego Gutiérrez Marañón'
author = 'Diana Isabel de Horna Cicka, Diego Gutiérrez Marañón'

# The full version, including alpha/beta/rc tags
release = 'CC-BY-SA'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

#Default file
master_doc = 'index'



# -- Options for HTML output -------------------------------------------------
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pyramid'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

 
 #Pdf generation

latex_engine = 'xelatex'
#latex_documents = ('index', 'test', 'TEST', 'Diana')
latex_show_pagerefs = True
latex_elements = {
     'papersize': 'a4paper',
     'pointsize': '12pt',
     'pxunit': '',
     'passoptionstopackages': '',
     'babel': '',
     'fontpkg': '\\usepackage[sfdefault]{roboto}',  #\usepackage[default,oldstyle,scale=0.95]{opensans}
     'fncychap': '',
     'preamble': '',
     'figure_align': '',
     'atendofbody': '',
     'extrapackages': '',
     'footer': '',
     'maketitle': '\\cover',
     'releasename': '0.0.1',
     'printindex': '',
     'fontenc': '',
     'inputenc': '',
     'classoptions': '',
     'utf8extra': '',
     
}

latex_documents = [
  ('index', 'music-for-geeks-and-nerds.tex', u'Music for Geeks and Nerds',
   u'Pedro Kroger', 'manual'),
]





