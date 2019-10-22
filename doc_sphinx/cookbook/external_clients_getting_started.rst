=====================================
External API Client: Getting Started
=====================================

..
    excerpt
        We offer our OpenAPI file to let you use it.
    endexcerpt

Not comfortable using HTTP request directly in your scripts? 
It's possible to use libraries in your favorite language.

Instead of this code:

.. code-block:: python

    response = requests.get('https://api.bimdata.io/cloud/12/project/58/ifc/985')
    ifc_list = response.json()


Your code could be:

.. code-block:: python

    ifc_list = bimdata_api_client.ifc_client.get_ifcs(cloud_pk=12, project_pk=58, id=985)


BIMData generate and maintain 2 clients: a Python lib and a Javascript lib.
You could also generate your own lib for any language. (See Generate it part of this content.)

Python
------

* URL: https://pypi.org/project/bimdata-api-client/
* Repository: https://github.com/bimdata/python-api-client

.. note:: info
    Requirements: Python 2.7 and 3.4+


Javascript
----------

* Install via NPM: ``npm install @bimdata/bimdata-api-client --save``
* URL: https://www.npmjs.com/package/@bimdata/bimdata-api-client


How-to find an API Client in my favourite language?
===================================================

We offer our OpenAPI file to let you use it.
You can use one of those generators to get a client in your favorite programmation language: https://openapi-generator.tech/docs/generators.html

Things to know about clients
-----------------------------

You will retrieve all the methods you need to interact with our API.

Generate it!
-------------

1. Install `OpenAPI Generator following their documentation`_
2. With a local version (or not) of our OpenAPI file, generate your client with ``openapi-generator generate`` options depending on your install.
#. Add your new API client in your software stack, everything is in the README generated along with your client.
#. Use it and :doc:`check our API Reference documentation </api/index>`.

.. _OpenAPI Generator following their documentation: https://openapi-generator.tech/docs/installation