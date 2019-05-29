===========
Guided Tour
===========

.. 
    excerpt
        Take a tour around and create your first application
    endexcerpt

==============================
1 - Which app will you create?
==============================

The implementation of your app depends on your needs.
You can create several types of applications.

Backend-less application
==========================

Chose this way if you are developping a backend-less application.

It could be the case, if you are working on **an app for tablet or mobile**.

Or maybe that your main programming language is Javascript.

➤ `Create a backend-less app`_

Application with a backend
===========================

With Users
-------------

Chose this way if your backend application benefit from **BIMData Connect users** credentials system.

Therefore, your users are able to share their data between multiple app.

It could be the case if they are sharing data between your app and BIMData Platform by example.

➤ `Create a backend app`_

Without Users
-------------

Chose this way if you don't want to use BIMData Connect users.

You have to handle authorization access yourself and will not be able to share data with other BIMData applications.
The basic setup is easier.

Our own BIMData Platform uses BIMData Connect users (backend-app with users).

➤ `Create a backend app`_



==================
2 - Authentication 
==================

For the authentication part, your application has to be registered on the BIMData Connect account manager.

What's an Access Token ?
=========================

The Client ID and the Client Secret are the 2 mandatory elements to get an Access Token from the Authentication Server.
You will need this Access Token for every call to the BIMData's API.


OpenID Connect
==============

To implement OpenID Connect within your application, find OpenID Connect libraries in your language : https://openid.net/developers/certified/


Flow Authentication
===================


.. note::

    To `learn more about the Authentication flows, read the Authentication guide page`_.




.. _learn more about the Authentication flows, read the Authentication guide page: ../topics/authentication_bimdata_connect.html

.. chapter 4

===================
3 - API Onboarding
===================

BIMData API is a tool to interact with your models stored on BIMData's servers.
Using the API, you can manage your projects, the clouds, upload your IFC files, manage them and retrieve and update data from your models through endpoints.

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
    To learn `more about the cloud, see the concept page`_ .


Filters
========

    .. include:: ../guide/filters.rst
       :start-after: excerpt
       :end-before: endexcerpt

.. note::  
    To learn `more about the filters, see the concept page`_ .

.. _more about the cloud, see the concept page: ../concepts/cloud.html
.. _more about the filters, see the concept page: ../concepts/filters.html

=======================
4 - Include the Viewer
=======================

See the dedicated page `Getting Started with the Viewer`_

.. _Getting Started with the Viewer: ../viewer/getting_started.html

====================
5 - Users Management
====================

There is currently 3 roles defined for Users.
Each User has a Role, and each User belongs to a Project.

Roles
=====

Users can have this Roles:

* admin
* user
* guest

Constant values in API
-----------------------

Using the API, there are constant values associated to roles. 
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
==================

Every User in the Cloud is linked to a Project.

Admin 
-------------

A cloud Admin can see every other member of the Cloud, can invite other Users as admin in the Cloud.

By default, the cloud Admin has admin rights on every project on the Cloud.

A cloud admin can ban any User from the Cloud.

.. warning::

    Ban a User exclude the User from all Projects of the Cloud. 

Member 
---------------

A Cloud member is at least a member of one Project.

User in the Project
===================

Any User in any Project can read the user list and see the other users of the project.


Admin 
-------------

A Project admin can invite Users to the Project.

.. note:: 

    The User is implicitly invited in the Cloud.

The Project admin manages the Roles of the Users: the admin car add, edit or delete Roles.


Member 
----------------

Can read and write EDM, model, and BCF.

Guest 
----------------

Can read-only : EDM, models, BCF and write BCF content.



.. _the User endpoint: |api_url|/doc#/user/getSelfUser

.. _Create a backend-less app: ../cookbook/2_create_nobackend_app.html
.. _Create a backend app: ../cookbook/2_create_backend_app.html
