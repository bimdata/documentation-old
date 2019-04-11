.. chapter 4

===============
API Onboarding
===============

BIMData API is a tool to interact with your models stored on BIMData's servers.
Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.

BIMData API follows this general principles:

* All API access is over HTTPS
* All non-binary data is sent and received as JSON
* Errors are sent using standard HTTP response codes (400, 404, 403)
* Actions are indicated by HTTP verbs: GET, POST, PUT, PATCH, DELETE
* All authentication is possible via OAuth2 bearer tokens


Cloud
======

    .. include:: ../concepts/cloud.rst
       :start-after: excerpt
       :end-before: endexcerpt

.. note::  
    To learn more about the `cloud, see the concept page`_ .


Filters
========

    .. include:: ../topics/filters.rst
       :start-after: excerpt
       :end-before: endexcerpt

.. note::  
    To learn more about the `filters, see the concept page`_ .

.. _cloud, see the concept page: ../concepts/cloud.html
.. filters, see the concept page: ../concepts/filters.html