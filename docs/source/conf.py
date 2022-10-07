# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.append(os.path.abspath('../../python'))



project = 'mymath.arithmetics'
copyright = '2022, Talha Ahmed'
author = 'Talha Ahmed'
release = version = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]


templates_path = ['_templates']
exclude_patterns = []

rst_prolog = '''
 .. |logo| image:: http://oatalha.github.io/_static/One-Animation-Logo-Small.png
             :alt: One Animation Logo
             :target: https://oatalha.github.io/

.. |repos| replace:: :doc:`REPOS<maindocs:repos>`
.. |apidocs| replace:: :doc:`APIDOCS<maindocs:repos>`

=========================== ============================ ================================
|logo|                      .. centered :: |repos|       .. centered :: |apidocs|
=========================== ============================ ================================
'''

autodoc_default_options = { 'members': True, 'undoc-members': True }
autodoc_mock_imports = []

autosummary_generate = True
autosummary_generate_overwrite = True
autosummary_imported_members = True
autosummary_ignore_module_all = True

autosectionlabel_prefix_document = True

todo_include_todos = True

intersphinx_mapping = {
        'maindocs': ('https://oatalha.github.io/', None)
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
