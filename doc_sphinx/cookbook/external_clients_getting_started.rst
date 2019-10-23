=====================================
External API Client: Getting Started
=====================================

..
    excerpt
        We offer our OpenAPI file to let you use it.
    endexcerpt

We generate and maintain 2 clients:

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