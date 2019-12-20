=====================================
External API Client: Getting Started
=====================================

..
    excerpt
        We offer our OpenAPI file to let you use it.
    endexcerpt

BIMData generate and maintain 2 clients: a Python lib and a Javascript lib.
You could also generate your own lib for any language. 

How-to find an API Client in my favourite language?
====================================================

Do you prefer using HTTP requests directly in your scripts? 
You can use a library in your favorite language.

Instead of this code:
------------------------

.. code-block:: python

    response = requests.get('https://api.bimdata.io/cloud/12/project/58/ifc/985')
    ifc_list = response.json()


Your code could be:
------------------------

.. code-block:: python

    ifc_list = bimdata_api_client.ifc_client.get_ifcs(cloud_pk=12, project_pk=58, id=985)


Python Client Lib
==========================

* URL: https://pypi.org/project/bimdata-api-client/
* Repository: https://github.com/bimdata/python-api-client

.. note:: info
    Requirements: Python 2.7 and 3.4+


Javascript Client Lib
==========================

* Install via NPM: ``npm install @bimdata/bimdata-api-client --save``
* URL: https://www.npmjs.com/package/@bimdata/bimdata-api-client


Generate it!
=============

We offer our OpenAPI file to let you use it.
You can use one of those generators to get a client in your favorite programmation language: https://openapi-generator.tech/docs/generators.html

1. Install `OpenAPI Generator following their documentation`_
2. With a local version (or not) of our OpenAPI file, generate your client with ``openapi-generator generate`` options depending on your install.
#. Add your new API client in your software stack, everything is in the README generated along with your client.
#. Use it and :doc:`check our API Reference documentation </api/index>`.

Things to know about clients
-----------------------------

You will retrieve all the methods you need to interact with our API.



.. _OpenAPI Generator following their documentation: https://openapi-generator.tech/docs/installation