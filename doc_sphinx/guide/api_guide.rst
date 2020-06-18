==================
BIMData API Guide
==================
..
    excerpt
        Discover BIMData's API documentation
    endexcerpt

Overview
==========

BIMData API is a tool to interact with your models stored on BIMData's servers.
One your account on BIMData Connect is created, you can:

* Create and manage clouds
* Create and manage projects
* Upload IFC files
* Request data from clouds, projects, and models


.. image:: /_images/guide/api_features.png
    :scale: 60 %
    :alt: Map of main features of the API


API Basics
================

BIMData API follows these general principles:

* All API access is over HTTPS
* All non-binary data is sent and received as JSON
* Errors are sent using standard HTTP response codes (400, 404, 403)
* Actions are indicated by HTTP verbs: GET, POST, PUT, PATCH, DELETE
* All authentication is possible via OAuth2 bearer tokens

.. warning::
    
    Calls made over plain HTTP will respond a 302, redirecting to the same URL over HTTPS.

The API Endpoint is: |api_url|


API Reference
--------------

Just looking for the API Reference?
Our API Reference presents Paramaters for the Requests, includes examples of Responses and Fields details for every objects.

.. raw:: html

    <a href="../api/index.html" class="bimdata-btn bimdata-btn__fill bimdata-btn__fill--primary bimdata-btn__radius">Go to API Reference</a>


Tools
=======

API Playground
---------------

You would like to try our API? 

Gladly, we provide you an interactive playground, based on OpenAPI files.

Try now your request on the :doc:`playground <../api_playground/apis>`!


Postman collections
---------------------

BIMData released a Postman Collection for you to enjoy and try our API in your usual software.

More about our :doc:`Postman collections <../getting_started/postman>`


External libraries
----------------------

We're currently maintaining two external libraries:

 * Our `external lib in JavaScript`_
 * Our `external lib in Python`_.

They are auto-generated from `our OpenAPI specification file`_ using the `openapi-generator`_ tool.

.. seealso::
    
    More details in the :doc:`documentation about External libraries <../getting_started/api_external_clients>`

Filtering
============

You can filter the responses of most endpoints using the filters.

Read the :doc:`Filter Guide <../guide/api_filters>`.


Tutorials
==========

Read our tutorials to begin using the API with a real-life sized purpose.


.. include:: ../tutorials/api_retrieve-elements.rst
    :start-after: excerpt
    :end-before: endexcerpt

:doc:`Get elements with IFC API <../tutorials/api_retrieve-elements>`

.. include:: ../tutorials/api_use_viewer_with_uploaded_models.rst
    :start-after: excerpt
    :end-before: endexcerpt

:doc:`Use the API with the Viewer <../tutorials/api_use_viewer_with_uploaded_models>`


.. seealso::
    
    See :doc:`all the Tutorials <../tutorials/index>`


.. _external lib in JavaScript: https://www.npmjs.com/package/@bimdata/bimdata-api-client
.. _external lib in Python: https://pypi.org/project/bimdata-api-client/
.. _our OpenAPI file: https://api.bimdata.io/doc#/
.. _openapi-generator: https://github.com/OpenAPITools/openapi-generator