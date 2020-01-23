====================
API Guide
====================
..
    excerpt
        Discover BIMData's API documentation
    endexcerpt

.. contents::
   :local:
   :depth: 1

Reference
==============

Just looking for the API Reference?

.. raw:: html

   <a href="/api/index.html" class="bimdata-btn bimdata-btn__fill bimdata-btn__fill--primary bimdata-btn__radius">Go to API Reference</a>

Our API, what's for?
=====================

BIMData.io let you access to your clouds, projects and all the data in your IFC files through the API.
One your account on BIMData Connect is created, you can:

* Create and manage clouds
* Create and manage projects
* upload IFC file
* request data from clouds, projects, and models

Discover the parts of the API:

* IFC API
* Collaboration API
* BCF API
* SSO API
* Webhook API
* Checker API


Endpoints
================

The API URL is |api_url|
All API requests must be made over HTTPS.

.. NOTE::
    Calls made over plain HTTP will respond a 302, redirecting to the same URL over HTTPS.

API Endpoint
------------
.. parsed-literal::
    |api_url|


Tutorials
==================

Read our tutorials to begin using the API with a real-life sized purpose

* `Get data from model into an Excel file`_

.. include:: ../tutorials/export_excel.rst
    :start-after: excerpt
    :end-before: endexcerpt

* `Retrieve elements following a constraint`_

.. include:: ../tutorials/retrieve-elements.rst
    :start-after: excerpt
    :end-before: endexcerpt

Explore the API
===============

Playground
-----------

You would like to try our API? Gladly, we provide you some `playground`_, based on OpenAPI files : `check it out`_!


Postman collection
-------------------

Explore the API, try it with the Postman collection.

.. image:: https://run.pstmn.io/button.svg
   :alt: Run in Postman!
   :target: https://app.getpostman.com/run-collection/3d3c0b2a685505934729

:doc:`Check our guide to get started with our Postman collection </cookbook/postman_getting_started>`.

Libraries
================

We're currently maintaining two external libraries:

 * Our `external lib in JavaScript`_
 * Our `external lib in Python`_.

They are auto-generated from `our OpenAPI file`_ with `openapi-generator`_.


.. _external lib in JavaScript: https://www.npmjs.com/package/@bimdata/bimdata-api-client
.. _external lib in Python: https://pypi.org/project/bimdata-api-client/
.. _our OpenAPI file: https://api.bimdata.io/doc#/
.. _openapi-generator: https://github.com/OpenAPITools/openapi-generator

.. _Go to API Reference: ../api/index.html
.. _Get data from model into an Excel file: ../tutorials/export_excel.html
.. _Retrieve elements following a constraint: ../tutorials/retrieve-elements.html
.. _playground: ../api_playground/index.html
.. _check it out:  ../api_playground/index.html





.. toctree::

    getting_started
    going_further
    api_details
    bcf_api
    collaboration_api
    sso_api