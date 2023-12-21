# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MOSQITO'
copyright = '2023, Green Forge Coop'
author = 'Green Forge Coop'
release = '1.1.1'

import os
import sys
sys.path.insert(0, os.path.abspath(".."))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'matplotlib.sphinxext.plot_directive',
    'matplotlib.sphinxext.mathmpl',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_favicon = 'source/_static/favicon.ico'
html_theme = 'pydata_sphinx_theme'
html_title = "MOSQITO manual"
html_last_updated_fmt = '%b %d, %Y'
html_context = {"default_mode": "light"}
html_use_modindex = True
html_copy_source = False
html_domain_indices = False
html_file_suffix = '.html'
htmlhelp_basename = 'mosqito'
html_css_files = ['source/_static/custom.css',
]

html_theme_options = {
  "logo": {
      "text": "MOSQITO",
      "image_light": 'source/_static/logo.png',
      "image_dark": 'source/_static/logo.png',
  },
  "github_url": "https://github.com/Eomys/MoSQITo",
  "collapse_navigation": True,
}


autosummary_generate = True
add_module_names = False

autodoc_default_options = {
    'members': True,
    # The ones below should be optional but work nicely together with
    # example_package/autodoctest/doc/source/_templates/autosummary/class.rst
    # and other defaults in sphinx-autodoc.
    'show-inheritance': True,
    'inherited-members': True,
    'no-special-members': True,
}

