"""Sphinx configuration."""
project = "Keggscherize"
author = "Elisa Marquez-Zavala"
copyright = "2025, Elisa Marquez-Zavala"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
