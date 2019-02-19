# -*- coding: utf-8 -*-
#
import os

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinxprettysearchresults",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "BIMData Documentation"
copyright = "2018, BIMData"
author = "BIMData"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# The short X.Y version.
version = "dev"
# The full version, including alpha/beta/rc tags.
release = "dev"

# sphinx-contrib
scv_whitelist_branches = os.environ.get("WHITELIST_BRANCHES", ".*").split(",")

API_URL = os.environ.get("API_URL", "https://api-staging.bimdata.io")
CDN_URL = os.environ.get("CDN_URL", "https://cdn-staging.bimdata.io")

language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
pygments_style = "monokai"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# html_theme = "classic"

html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": False,
    "titles_only": False,
}

html_style = "css/my_theme.css"
html_file_suffix = None
html_context = {
    "github_user": "bimdata",
    "github_repo": "documentation",
    "display_github": True,
    "conf_py_path": "doc_sphinx/",
    "source_suffix": ".rst",
    "github_version": "dev/",
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/_images/logo-bimdata-darkbg.svg"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/_images/bimdata_favico.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "_images"]

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {"**": ["globaltoc.html", "sourcelink.html", "searchbox.html"]}

html_domain_indices = True
html_use_index = True
html_split_index = True
html_show_sourcelink = True
html_show_sphinx = True
html_file_suffix = ".html"
html_link_suffix = ".html"

# Language to be used for generating the HTML full-text search index.
html_search_language = "en"

# Output file base name for HTML help builder.
htmlhelp_basename = "BimdataSphinxdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "BimdataSphinx.tex",
        "BIMData Sphinx Documentation",
        "bimdata",
        "manual",
    )
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "bimdatasphinx", "BIMData Sphinx Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "BimdataessaiSphinx",
        "BIMData essai Sphinx Documentation",
        author,
        "BimdataessaiSphinx",
        "One line description of project.",
        "Miscellaneous",
    )
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"https://docs.python.org/": None}

swagger2sphinx_swagger_location = "api/swagger.json"
# swagger2sphinx_swagger_location = "http://example.com/swagger.json"

# Autosummary issue resolver
numpydoc_show_class_members = False