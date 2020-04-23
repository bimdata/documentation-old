# -*- coding: utf-8 -*-
#
import os
import re

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "1.8"

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
    "sphinx_substitution_extensions",
    "sphinx_copybutton",
    "sphinxcontrib.contentui"
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

version = ""
# The full version, including alpha/beta/rc tags.
release = "1.0"

# sphinx-contrib
scv_whitelist_branches_regexp = [
    re.compile(regexp)
    for regexp in os.environ.get("WHITELIST_BRANCHES_REGEXP", "").split(",")
    if regexp != ""
]

scv_whitelist_branches_name = os.environ.get(
    "WHITELIST_BRANCHES_NAME", "master,dev,tech-writing"
).split(",")

scv_whitelist_branches = tuple(scv_whitelist_branches_name + scv_whitelist_branches_regexp)


API_URL = os.environ.get("API_URL", "https://api-staging.bimdata.io")
CDN_URL = os.environ.get("CDN_URL", "https://cdn-staging.bimdata.io")
CONNECT_URL = os.environ.get("CONNECT_URL", "https://login-staging.bimdata.io")
IAM_URL = os.environ.get("IAM_URL", "https://iam-next.bimdata.io/auth/realms/bimdata/protocol/openid-connect/token")
PLAYGROUND_CLIENT_ID = os.environ.get("PLAYGROUND_CLIENT_ID", "719549")

# replace in code
substitutions = [
    ("|api_url|", API_URL),
    ("|cdn_url|", CDN_URL),
    ("|bimdata_connect|", CONNECT_URL),
    ("|iam_url|", IAM_URL),
]

# replace in text
rst_prolog = f"""
.. |api_url| replace:: {API_URL}
.. |cdn_url| replace:: {CDN_URL}
.. |bimdata_connect| replace:: {CONNECT_URL}
.. |iam_url| replace:: {IAM_URL}
"""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None
# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = []

HAS_ROBOTS_TXT = os.environ.get("HAS_ROBOTS_TXT", "true")
if HAS_ROBOTS_TXT == "true":
    html_extra_path.append("_static/robots.txt")

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.rst", "node_modules", ".v_env"]

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


def setup(app):
    app.add_stylesheet("css/style.css")  # also can be a full URL


html_file_suffix = None
html_context = {
    "github_user": "bimdata",
    "github_repo": "documentation",
    "display_github": True,
    "conf_py_path": "doc_sphinx/",
    "source_suffix": ".rst",
    "github_version": "dev/",
    "api_url": API_URL,
    "cdn_url": CDN_URL,
    "connect_url": CONNECT_URL,
    "playground_client_id": PLAYGROUND_CLIENT_ID,
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = "_static/_images/bimdata_logo-doc.svg"

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
html_title = "BIMData Doc"

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None


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

html_sidebars = {"**": ["globaltoc.html"]}


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

# -- Options for LaTeX output ------------------------------------------------

latex_engine = "xelatex"
# latex_engine = "pdflatex"

preamble = r"""
%%%%%%%%%%%%%%%%%%%% Meher %%%%%%%%%%%%%%%%%%
%%%add number to subsubsection 2=subsection, 3=subsubsection
%%% below subsubsection is not good idea.
\setcounter{secnumdepth}{3}
%
%%%% Table of content upto 2=subsection, 3=subsubsection
\setcounter{tocdepth}{2}

\usepackage{amsmath,amsfonts,amssymb,amsthm}
\usepackage{graphicx}

%%% reduce spaces for Table of contents, figures and tables
%%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
\usepackage[notlot,nottoc,notlof]{}


\usepackage{xcolor}
\usepackage{sectsty}

\definecolor{primary}{RGB}{47,55,74}
\definecolor{secondary}{RGB}{249,199,44}

\chapterfont{\color{primary}}  % sets colour of chapters
\sectionfont{\color{primary}}  % sets colour of sections
\subsectionfont{\color{primary}} % sets colour of subsections

\usepackage{transparent}
\usepackage{eso-pic}
\usepackage{lipsum}

\usepackage{footnotebackref} %%link at the footnote to go to the place of footnote in the text

%% spacing between line
\usepackage{setspace}
%%%%\onehalfspacing
%%%%\doublespacing
\singlespacing

%%%%%%%%%%% datetime
\usepackage{datetime}

\newdateformat{MonthYearFormat}{%
    \monthname[\THEMONTH], \THEYEAR}

%% RO, LE will not work for 'oneside' layout.
%% Change oneside to twoside in document class
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}

%%% Alternating Header for oneside
\fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
\fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}

%%% page number
\fancyfoot[CO, CE]{\thepage}

\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\headrule}{\hbox to\headwidth{%
  \color{secondary}\leaders\hrule height \headrulewidth\hfill}}

\renewcommand{\footrulewidth}{0.5pt}
\renewcommand{\footrule}{\hbox to\headwidth{%
  \color{secondary}\leaders\hrule height \headrulewidth\hfill}}

\RequirePackage{tocbibind} %%% comment this to remove page number for following
\addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
\addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
\addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
% \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}

%%reduce spacing for itemize
\usepackage{enumitem}
\setlist{nosep}

%%%%%%%%%%% Quote Styles at the top of chapter
\usepackage{epigraph}
\setlength{\epigraphwidth}{0.8\columnwidth}
\newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}

%%%%%%%%%%% Quote for all places except Chapter
\newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}

%%%%%%%%%%% Set fonts for all the main texts
\usepackage{fontspec}
\setmainfont[BoldFont={Roboto-Bold.ttf},
ItalicFont={Roboto-LightItalic.ttf},
BoldItalicFont={Roboto-BoldItalic.ttf}
]{Roboto-Light.ttf}
"""


mktitle = r"""
\pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

\begin{titlepage}
    \centering

    \vspace*{40mm} %%% * is used to give space from top
    \textbf{\Huge {Sphinx Documentation}}

    \vspace{0mm}
    \begin{figure}[!h]
        \centering
        \includegraphics[scale=0.3]{../../_images/bimdata-doc-logo.png}
    \end{figure}

    \vspace{0mm}
    \Large \textbf{{Team BIMData}} %%% Change to contact@bimdata ?

    \small Created on : July, 2019

    \vspace*{0mm}
    \small  Last updated : \MonthYearFormat\today


    %% \vfill adds at the bottom
    \vfill
    \small \textit{More documents are freely available at }{\href{https://developers.bimdata.io/}{bimdata.io}}
\end{titlepage}

%% \clearpage
%% \pagenumbering{roman}
%% \tableofcontents
%% \listoffigures
%% \listoftables
\clearpage
\pagenumbering{arabic}
"""

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "a4paper",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    "fncychap": "\\usepackage{fncychap}",
    "fontpkg": "\\usepackage{amsmath,amsfonts,amssymb,amsthm}",
    "figure_align": "htbp",
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "12pt",
    # Additional stuff for the LaTeX preamble.
    "preamble": preamble,
    # No default title
    # "maketitle": "",
    "maketitle": mktitle,
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    "sphinxsetup": "hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0.1843137254902,0.2156862745098,0.29019607843137}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0.1843137254902,0.2156862745098,0.29019607843137}, \
        OuterLinkColor={rgb}{0.1843137254902,0.2156862745098,0.29019607843137}",
    "tableofcontents": " ",
    # No default toc
    # "tableofcontents": "",
      'extraclassoptions': 'openany,oneside',
}

latex_show_urls = "footnote"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "platform/index",
        "BIMData_documentation.tex",
        "BIMData Sphinx Documentation",
        "BIMData",
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
