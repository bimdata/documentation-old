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


1 - Which app will you create?
==============================

The implementation of your app depends on your needs.
You can create several types of applications.

Backend-less application
------------------------

Chose this way if you are developing a backend-less application.

These applications:
  - could share data with other applications like BIMData Platform or any other third-party app.
  - must use **BIMData Connect users** credentials system.
  - are usually mobile apps or small Javascript apps.

➤ :doc:`Create a backend-less app <../tutorials/dev_create_an_application>`

Application with a backend
--------------------------

With BIMData Connect Users
~~~~~~~~~~~~~~~~~~~~~~~~~~

Chose this way if your app has a backend (PHP, NodeJS, Python, .NET, etc.).

These applications:
  - could share data with other applications like BIMData Platform or any other third-party app.
  - must use **BIMData Connect users** credentials system.

.. note
    Our own BIMData Platform application uses BIMData Connect users (backend-app with users).

➤ :doc:`Create an application <../tutorials/dev_create_an_application>`

Without Users
~~~~~~~~~~~~~

Chose this way if you don't want to use BIMData Connect users.
See :doc:`how-to create an IFC Access Token <../tutorials/dev_ifc_access_token>`

These applications:
  - have to manage their own users and authorizations
  - can't share data with other BIMData applications
  - have an easier setup

.. note::

    Your user has no access to what your application created. To grant access to your user see :doc:`how-to share data with your app <../tutorials/api_share_data_app_platform>`


➤ :doc:`Create a backend app <../tutorials/dev_create_an_application>`


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


