=========================
Documentation BIMData
=========================

Sphinx:
=======
Sphinx is used to generate static HTML documentation pages.
The configuration file ``conf.py`` contains the settings for the build of our Sphinx edition.
The ``requirements.txt`` file lists all the extensions used for this Sphinx documentation.

Having a directory to store the generated pages named html_doc and in the same parent dir than sphinx_doc directory, the build command should be:

``$> sphinx-build -b html . ../html_doc``

Redoc:
=======
Redoc is in its own separate directory.
Redoc directory contains:

* Redoc JS library file
* OpenAPI file
* HTML file to support JS processing OAS file