# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Serika.dev API Documentation'
copyright = '2024, Serika.dev'
author = 'Serika.dev'

# -- General configuration ---------------------------------------------------

    'myst_parser',
    'sphinx_rtd_theme',

    'sphinx_tabs.tabs',
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



# -- Sphinx Design configuration ---------------------------------------------
# No specific configuration needed for basic usage
