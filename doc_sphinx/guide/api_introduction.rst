===============
BIMData's API
===============

..
    excerpt
        Discover BIMData's API documentation
    endexcerpt

API Reference
==============

Just looking for the API Reference?

.. raw:: html

   <a href="../api/index.html" class="bimdata-btn bimdata-btn__fill bimdata-btn__fill--primary bimdata-btn__radius">Go to API Reference</a>


Introduction
================

BIMData.io let you access to your clouds, projects and all the data in your IFC files through the API.
One your account on BIMData Connect is created, you can:

* Create and manage clouds
* Create and manage projects
* upload IFC file
* request data from clouds, projects, and models


URL
================

The API URL is |api_url|

All API requests must be made over HTTPS.

.. NOTE::
    Calls made over plain HTTP will respond a 302, redirecting to the same URL over HTTPS.

API Enpoint
------------
.. parsed-literal::
    |api_url|



Our Tutorial
==============

Read our tutorial to begin using the API with a real-life sized purpose


* `Retrieve elements following a constraint`_

.. include:: ../tutorials/api_retrieve-elements.rst
    :start-after: excerpt
    :end-before: endexcerpt

Playground
===========

You would like to try our API? Gladly, we provide you some `playground`_, based on OpenAPI files : `check it out`_!


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
.. _Retrieve elements following a constraint: ../tutorials/api_retrieve-elements.html
.. _playground: ../api_playground/index.html
.. _check it out:  ../api_playground/index.html


