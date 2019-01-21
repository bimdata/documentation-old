=========================
Documentation BIMData
=========================

Welcome to the BIMData's documentation git repository.

After cloning the git repository, to build your own local version, having a directory to store the generated pages named ``html_doc``, in the same parent dir than ``sphinx_doc`` directory, the build command should be:

``$> sphinx-versioning build -r {branch_name} doc_sphinx html_doc``

Branches
=========

We work with 3 branches, currently named *master*, *dev* and *tech-writing*:

* *master*: latest and stable version of the documentation
* *dev*: testing before putting the new content in ``master`` and tests for new features of the documentation
* *tech-writing*: content under edition. This branch is hosting Work In Progress and is not fully polished.

Sphinx:
=======

We are using Sphinx to generate our documentation.
The configuration file ``conf.py`` contains the settings for the build of our Sphinx edition. 

Note: we are using Python3. To be able to use Python3 and the context of working on the documentation, you can use `Virtualenv <https://virtualenv.pypa.io/en/stable/installation/>`_.

The ``requirements.txt`` file lists all the extensions used for this Sphinx documentation.
You can use:

``$> pip install -r doc_sphinx/requirements.txt``

Customization
---------------

For the version switcher, we are using `the sphinx-versioning extension <https://robpol86.github.io/sphinxcontrib-versioning/>`_.
The theme is the `sphinx-rtd-theme <https://sphinx-rtd-theme.readthedocs.io>`_.

Redoc:
=======

Our API Reference is served by `Redoc <https://rebilly.github.io/ReDoc/>`_ in its own separate directory.
Redoc directory contains:

* the Redoc JS library file
* our OpenAPI file
* an HTML file to support JS processing OAS file