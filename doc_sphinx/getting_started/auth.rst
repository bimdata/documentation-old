===============
Authentication
===============
..
    excerpt
        Overview of the authentication process for developers
    endexcerpt


.. contents:: In this page
   :depth: 2

Before you start coding
=======================

You are excited to do your first calls through the API or to view your Models in the 3D Viewer embedded in your app?
Before you start coding, you must create an account and set up an application to get your Access Token.

Create your BIMData Connect account
----------------------------------------

Go `to BIMData Connect <https://connect.bimdata.io/>`_, fill the registration form. 

You join to the BIMData Connect homepage immediately.
Create your first cloud and your first project.


Create your app
----------------

From the BIMData Connect homepage, you create your application.

Follow :doc:`the create your application Tutorial <tutorials/dev_create_an_application>`.

The Secret ID is yours and should never be shared.


Useful tools
=============

To try to authenticate with your credentials, you can:

* Try it on the :doc:`API Playground </api_playground/index>`
* Use :doc:`our Postman collection <postman>`
* Use the API with :doc:`external tools <api_external_clients>`

oAuth usage
============

oAuth is the protocol we use to authenticate your credentials.

OpenID Flows
-------------

OpenID Connect is an identity layer on top of the OAuth 2.0 protocol.
OpenID Connect provides different authentication flows. You have to choose the one which fits your needs the best.

BIMData Connect implements two OpenID flows:

* Authorization code flow
* Implicit flow

See :doc:`the Authorization Flows content </guide/authentication_flows>` to learn more.

My user or my app?
^^^^^^^^^^^^^^^^^^

When you try to access Models, is it the App or the User credentials used?
If you want your user to access Models, you have to invite the User to the Cloud where your Models are, otherwise, no Model will be readable for the User.

See :doc:`the tutorial about sharing data with your application </tutorials/api_share_data_app_platform>`



.. seealso::

    See the :doc:`how to log in BIMData with your own Active Directory, LDAP or OpenID Connect service <../guide/auth_identity_providers>`


Scopes
-------

Scopes are a way to let your application access to the data. 
A scope is a limitation to the data on a given resource.

Read :doc:`our documentation about Scopes <../guide/concepts/scopes>`.


.. seealso::

    * Tutorial: :doc:`Retrieve your Models </tutorials/api_retrieve-elements.rst>`
    * :doc:`How-to display your Models in the 3D Viewer </tutorials/using_custom_viewer.rst>`
    * Tutorial: :doc:`Create your first plugin for the 3D Viewer </tutorials/viewer_create_plugin.rst>`

