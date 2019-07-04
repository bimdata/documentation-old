===============
BIMData's API
===============


Introduction
================

The Bimdata API is organized around `REST`_. Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. 
We use built-in HTTP features, like HTTP authentication and HTTP verbs, which are understood by off-the-shelf HTTP clients. 
We support `cross-origin resource sharing`_, allowing you to interact securely with our API from a client-side web application (though you should never expose your secret API key in any public website's client-side code).
JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.


BIMData.io let you access to your clouds, projects and all the data in your IFC files through the API.
One your account on BIMData Connect is created, you can:

* Create and manage clouds
* Create and manage projects
* upload IFC file
* request data from clouds, projects, and models

API Reference
==============

:Just looking for the API Reference?: `Go to API Reference`_


URL
================

The API URL is **https://api-beta.bimdata.io**
All API requests must be made over HTTPS. 

.. NOTE::
    Calls made over plain HTTP will respond a 302, redirecting to the same URL over HTTPS.

API Enpoint
------------
.. parsed-literal::
    https://api-beta.bimdata.io

Content-Type
================

Endpoints usually only accept ``application/json`` content type.
Endpoints used for files upload use ``application/x-www-form-urlencoded`` (aka form-data) content type.


Our Tutorials
==============

Read our tutorials to begin using the API with a real-life sized purpose

* `Get data from model into an Excel file`_

.. include:: ../tutorials/export_excel.rst
    :start-after: excerpt
    :end-before: endexcerpt

* `Retrieve elements following a constraint`_

.. include:: ../tutorials/retrieve-elements.rst
    :start-after: excerpt
    :end-before: endexcerpt

Playground
===========

:You would like to try our API?: Gladly, we provide you some `playground`_, based on OpenAPI files : `check it out`_!


Libraries
================

We're currently maintaining two external libraries:
* Our `external lib in JavaScript`_ 
* Our `external lib in Python`_. 

They are auto-generated from `our OpenAPI file`_ with `swagger-codegen`_.


.. _REST: https://en.wikipedia.org/wiki/Representational_state_transfer
.. _cross-origin resource sharing: https://en.wikipedia.org/wiki/Cross-origin_resource_sharing

.. _external lib in JavaScript: https://www.npmjs.com/package/@bimdata/bimdata-api-client
.. _external lib in Python: https://pypi.org/project/bimdata-api-client/
.. _our OpenAPI file: https://api-beta.bimdata.io/doc
.. _swagger-codegen: https://swagger.io/

.. _Go to API Reference: ../api/
.. _Get data from model into an Excel file: ../tutorials/export_excel.html
.. _Retrieve elements following a constraint: ../tutorials/retrieve-elements.html
.. _playground: ../api_partial/index.html
.. _check it out:  ../api_partial/index.html