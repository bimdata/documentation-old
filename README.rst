=========================
Documentation BIMData
=========================

Welcome to the BIMData's documentation git repository.

After cloning this git repository, build your own local version:

``~: cd doc_sphinx && sphinx-build -b html . ../html_doc``


.. image:: doc_sphinx/_images/bimdata_homepage_small.png

.. image:: https://img.shields.io/github/issues-pr/bimdata/documentation?color=%23f9c72c
    :alt: GitHub pull requests

Branches
=========

We work with 2 main branches, currently named *master* and *develop*:

* *master*: latest and stable version of the documentation
* *develop*: base branch for branches with content under edition. This branch is hosting upcoming documentation.

Sphinx:
=======

We are using Sphinx to generate our documentation.
The configuration file ``conf.py`` contains the settings for the build of our Sphinx edition.

Note: we are using Python3. To be able to use Python3 and the context of working on the documentation, you can use `Virtualenv <https://virtualenv.pypa.io/en/stable/installation/>`_.

The ``requirements.txt`` file lists all the extensions used for this Sphinx documentation.
To install all the dependencies, use:

``~:  pip install -r doc_sphinx/requirements.txt``


Customization
---------------

The Sphinx theme is custom and based on the `sphinx-rtd-theme <https://sphinx-rtd-theme.readthedocs.io>`_.


API Documentation:
===================

Our API Reference is served by `Spectacle <https://github.com/sourcey/spectacle/>`_ in the directory named `api/`.

The API Documentation build command is:

``~:  cd doc_sphinx && npm run build:apiref``


Contribute to this project:
===========================

Create a branch based on ``develop`` and push it as a Pull Request in the repository.


Tests:
======

Launch the test suite:

``~: cd doc_sphinx && npm test``


Licence:
========

.. image:: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg


This documentation is under Creative Commons: `Attribution 4.0 International (CC BY 4.0) <http://creativecommons.org/licenses/by/4.0/>`_  