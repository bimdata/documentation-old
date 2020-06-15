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

:doc:`The API Playground </api_playground/index>`

*  The Playground is based on Swagger UI. After authentication with your credentials, you can try the endpoints with parameters.

:doc:`Our Postman collection <postman>`

*  BIMData maintains a Postman collection usable in your environment Postman to make your requests.

:doc:`Use external libraries <api_external_clients>`

*  Generate your API clients from our OpenAPI specification.


oAuth usage
============

:doc:`OpenID Flows </guide/authentication_flows>`

* oAuth is the protocol we use to authenticate your credentials.
* OpenID Connect is an identity layer on top of the OAuth 2.0 protocol.
 OpenID Connect provides different authentication flows. You have to choose the one which fits your needs the best.
* BIMData Connect implements two OpenID flows:
   * Authorization code flow
   * Implicit flow

:doc:`Scopes <../guide/concepts/scopes>`

* Scopes are a way to let your application access to the data. A scope is a limitation to the data on a given resource.

:doc:`My user or my app? </tutorials/api_share_data_app_platform>`

* When you try to access Models, is it the App or the User credentials used? If you want your user to access Models, you have to invite the User to the Cloud where your Models are, otherwise, no Model will be readable for the User.

:doc:`Connect your identity provider </guide/auth_identity_providers>`

* Want to log in BIMData with your own Active Directory, LDAP or OpenID Connect service? It's possible.

.. seealso::

    * Tutorial: :doc:`Retrieve your Models </tutorials/api_retrieve-elements.rst>`
    * :doc:`How-to display your Models in the 3D Viewer </tutorials/using_custom_viewer.rst>`
    * Tutorial: :doc:`Create your first plugin for the 3D Viewer </tutorials/viewer_create_plugin.rst>`
