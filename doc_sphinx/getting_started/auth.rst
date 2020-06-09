===============
Authentication
===============
..
    excerpt
        Overview of the authentication process for developers
    endexcerpt


.. contents::

Before you start coding
=======================

You are excited to do your first calls through the API or to view your Models in the 3D Viewer embedded in your app?
Before you start coding, you must create an account and set up an app to get your Acces Token.

Create your BIMData Connect account
----------------------------------------

Go to BIMData Connect, fill the registration form.


Create your app
----------------

See :doc:`the create your application Tutorial <tutorials/dev_create_an_application>`.

The Secret ID is yours and should not be shared.


Useful tools
=============

To try to authenticate with your account or your app credentials, you can:

* Try it on the :doc:`API Playground </api_playground/index>`
* Use :doc:`our Postman collection <postman>`
* Use the API with :doc:`external tools <api_external_clients>`

oAuth usage
============

oAuth is the protocol we use to authenticate your credentials.

.. seealso::

    See the :doc:`how to log in BIMData with your own Active Directory, LDAP or OpenID Connect service <../guide/auth_identity_providers>`


Scopes
======

Scopes are a way to let your application access to the data.


OpenID Flows
=============

OpenID Connect is an identity layer on top of the OAuth 2.0 protocol.
OpenID Connect has different authentication flows and you have to choose the one which fits your needs the best.

There is:
* Authorization code flow
* Implicit flow

My user or my app?
-------------------

When you try to access Models, is it the App or the User credentials used?
If you want your user to access Models, you have to invite the User to the Cloud where your Models are, otherwise no Model will be readable for the User.


.. seealso::

    Retrieve your Models

    Display your Models in the 3D Viewer

    Create plugins for the 3D Viewer

