=========================
Documentation BIMData
=========================

Welcome to the BIMData's documentation git repository.

After cloning this git repository, build your own local version:

``$> cd doc_sphinx && sphinx-build -b html . ../html_doc``


.. image:: doc_sphinx/_images/bimdata_homepage_small.png

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
To install all the dependencies, use:

``$> pip install -r doc_sphinx/requirements.txt``


Customization
---------------

The Sphinx theme is custom and based on the `sphinx-rtd-theme <https://sphinx-rtd-theme.readthedocs.io>`_.


API Documentation:
===================

Our API Reference is served by `Spectacle <https://github.com/sourcey/spectacle/>`_ in the directory named `api/`.

The API Documentation build command is:

``$> cd doc_sphinx && npm run build:apiref``


Tests:
======

Launch the test suite:

``$> cd doc_sphinx && npm test``


Licence:
========

This documentation is under Creative Commons: `Attribution 4.0 International (CC BY 4.0) <http://creativecommons.org/licenses/by/4.0/>`_  