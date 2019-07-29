=====================
Create backend app
=====================
.. 
    excerpt
        How-To create an application on BIMData Connect
    endexcerpt

.. image:: /_images/cookbook/BIMdata_create_application.png
   :scale: 50 %
   :alt: Create your application
   :align: right

Name
====

You can choose whatever you want. The name is displayed to users when requesting permissions and in their application list.

Client Type
===========

Confidential
You provide a secret token and it must stay secret. Never set this token in code executed client-side

.. note::
    
    Any string stored in the browser or mobile app can be found, even if the code is minified or compiled.

Response types
==============

code (Authorization Code Flow)
This means you will get a code and you will be able to trade it for an access_token

.. note::

    Read more about **Authorization code flow**: https://auth0.com/docs/flows/concepts/auth-code

Scopes
======

Select scopes your app needs (see `scopes`_ doc).

JWT algorithm
===============

Select: RS256

Website URL
===========

Users have access to this link if they want to know more about your application

Terms URL
=========

Users have access to the link to see your end-user license agreement

Logo
====

Your app logo. Users see it next to your app name

Redirect URIs
=============

List of authorized redirect URIs
After allowing your app to access their data, users will be redirected to your app on one of these URIs.
For security reasons, avoid using locals URL such as *localhost*, *127.0.0.1*, *192.168.x.x*, etc.

Post Logout URIs
================

List of authorized Post Logout URIs
Useful only if you want to implement an SSO logout

.. tip::

    See also :doc:`Authentication documentation </guide/authentication_bimdata_connect>`


.. _scopes: ../concepts/scopes.html
