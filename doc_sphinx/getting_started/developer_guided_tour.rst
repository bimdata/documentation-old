:orphan:

===========
Guided Tour
===========

..
    excerpt
        Take a tour around and create your first application
    endexcerpt

.. note:: 
   
    About the Guided Tour:

    * Topics: application, authentication, users management
    * Pre-requisites: REST API knowledge
    * Goal of this tutorial: give you an overall view of our software
    * 5 steps to follow

.. contents::
    :depth: 2




2 - Authentication
==================



3 - API Onboarding
===================



BIMData API is a tool to interact with your models stored on BIMData's servers.
Using the API, you can manage your projects, the clouds, upload your IFC files, manage them and retrieve and update data from your models through endpoints.

BIMData API follows these general principles:

* All API access is over HTTPS
* All non-binary data is sent and received as JSON
* Errors are sent using standard HTTP response codes (400, 404, 403)
* Actions are indicated by HTTP verbs: GET, POST, PUT, PATCH, DELETE
* All authentication is possible via OAuth2 bearer tokens

.. _api_onboarding_gt:

Cloud
-----

.. include:: ../concepts/cloud.rst
    :start-after: excerpt
    :end-before: endexcerpt

.. note::

    To learn :doc:`more about the cloud, see the concept page <../guide/concepts/cloud>`.


Filters
-------

.. include:: ../guide/filters.rst
    :start-after: excerpt
    :end-before: endexcerpt

.. note::

    To learn :doc:`more about the filters, see the concept page <../guide/api_filters>`.


4 - Include the Viewer
=======================

See the dedicated page :doc:`Getting Started with the Viewer <../viewer/index>` 


