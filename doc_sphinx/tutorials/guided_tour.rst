===========
Guided Tour
===========

..
    excerpt
        Take a tour around and create your first application
    endexcerpt


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

➤ `Create a backend-less app`_

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

➤ `Create a backend app`_

Without Users
~~~~~~~~~~~~~

Chose this way if you don't want to use BIMData Connect users.

These applications:
  - have to manage their own users and authorizations
  - can't share data with other BIMData applications
  - have an easier setup

➤ `Create a backend app`_




2 - Authentication
==================

For the authentication part, your application has to be registered on the BIMData Connect account manager (even if you're not using BIMData Connect users).

Depending on the type of app you have, you may use different ways to authenticate your app or your users.

Your goal is to retrieve an **Access Token**.

An **Access Token** is needed for every call to the BIMData's API. 
It represents your app, or a user using your app.

Retrieve an app Access Token
----------------------------

An application Access Token represents the app itself and is not linked to any user. 
It is used when you don't use **BIMData Connect** users or if you want to use `webhooks`_  or if you're doing some automated tasks.

.. note::

    See `Get Access Token documentation`_ for more information.


Retrieve a user Access Token
----------------------------

A user Access Token represents a user using your app. 
It means when you're calling the API with this token, you will get the data (clouds, projects, models, etc.) the user has access to.

Before you can retrieve a user Access Token, the user must explicitly allow your application to behave as the user.
There are multiple ways to ask them their consent, you can see them LINK TO OpenID Connect Authorization flows

.. note::

    See `Authentication Flow documentation`_



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


Cloud
-----

.. include:: ../concepts/cloud.rst
    :start-after: excerpt
    :end-before: endexcerpt

.. note::
    To learn `more about the cloud, see the concept page`_.


Filters
-------

.. include:: ../guide/filters.rst
    :start-after: excerpt
    :end-before: endexcerpt

.. note::
    To learn `more about the filters, see the concept page`_.

.. _more about the cloud, see the concept page: ../concepts/cloud.html
.. _more about the filters, see the concept page: ../concepts/filters.html


4 - Include the Viewer
=======================

See the dedicated page `Getting Started with the Viewer`_



5 - Users Management
====================

There are currently 3 roles defined for Users.
Each User has a Role, and each User belongs to a Project.

Roles
-----

Users can have these Roles:

* admin
* user
* guest

Constant values in API
~~~~~~~~~~~~~~~~~~~~~~

Using the API, there are constant values associated with roles.

See `the User endpoint`_ to learn about the usage.

.. note::

    These constants are only used in API.

When checking User's role through the API, the values are:

* Cloud role's values
   * admin: 100
   * user: 50

* Project role's values
   * admin: 100
   * user: 50
   * guest: 25


User in the Cloud
-----------------

Every User in the Cloud is linked to a Project.

Admin
~~~~~

A cloud Admin can see every other member of the Cloud, can invite other Users as admin in the Cloud.

By default, the cloud Admin has admin rights on every project on the Cloud.

A cloud admin can ban any User from the Cloud.

.. warning::

    Ban a User exclude the User from all Projects of the Cloud.

Member
~~~~~~~

A Cloud member is at least a member of one Project.

User in the Project
-------------------

Any User in any Project can read the user list and see the other users of the project.


Admin
~~~~~

A Project admin can invite Users to the Project.

.. note::

    The User is implicitly invited in the Cloud.

The Project admin manages the Roles of the Users: the admin car add, edit or delete Roles.


Member
~~~~~~

Can read and write DMS, model, and BCF.

Guest
~~~~~

Can read-only: DMS, models, BCF and write BCF content.


.. _the User endpoint: |api_url|/doc#/user/getSelfUser
.. _Getting Started with the Viewer: ../viewer/getting_started.html

.. _Create a backend-less app: ../cookbook/2_create_nobackend_app.html
.. _Create a backend app: ../cookbook/2_create_backend_app.html
.. _webhooks: ../guide/webhooks.html
.. _Get Access Token documentation: ../cookbook/get_access_token.html
.. _Authentication Flow documentation: ../guide/authentication_flows.html

.. toctree::
    :maxdepth: 1