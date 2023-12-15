# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'teamdocs'
copyright = '2023, GU Orbit Software Team'
author = 'GU Orbit Software Team'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'myst_parser',
    'sphinx_mdinclude',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['style']
html_css_files = ["custom.css"]

autodoc_typehints = "signature"
autodoc_typehints_description_target = "documented_params"

html_theme_options = {
    "dark_css_variables": {
        "color-api-background": "#202020",
        "color-api-background-hover": "#505050",
        "color-sidebar-item-background--current": "#303030",
        "color-sidebar-item-background--hover": "#303030",
    },
}
