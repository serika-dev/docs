# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Serika.dev API Documentation'
copyright = '2024, Serika.dev'
author = 'Serika.dev'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_hoverxref',
    'sphinx_design',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'requirements.txt']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- MyST Parser configuration -----------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# -- Sphinx Hoverxref configuration ------------------------------------------

hoverxref_auto_ref = True
hoverxref_domains = ['py', 'cite']
hoverxref_roles = [
    'option',
    'doc',
    'term',
]
hoverxref_role_types = {
    'hoverxref': 'modal',
    'ref': 'modal',
    'doc': 'modal',
    'class': 'tooltip',
    'func': 'tooltip',
    'meth': 'tooltip',
    'attr': 'tooltip',
    'exc': 'tooltip',
    'obj': 'tooltip',
    'mod': 'tooltip',
    'const': 'tooltip',
}

# -- Sphinx Design configuration ---------------------------------------------
# No specific configuration needed for basic usage
