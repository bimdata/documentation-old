========================
Create backend-less app
========================

.. 
    excerpt
        How-To create a mobile or tablet application on BIMData Connect
    endexcerpt

.. image:: /_images/cookbook/BIMdata_create_application.png
   :scale: 50 %
   :alt: Create your application
   :align: right

Name
=====

You can chose whatever you want. The name is displayed to users when requesting permissions and in their application list.

Client Type
===========

Public
As your app has no backend, you can't keep a secret token.

.. note::

    Any string stored in browser or mobile app can be found even if the code is minified or compiled.

Public
======

As your app has no backend, you can't keep a secret token. 
(Any string stored in the browser or mobile app can be found even if the code is minified or compiled)

Response types
==============

Select id_token token (Implicit Flow)
This means you will get an ``id_token`` (not used by BIMData) and an ``access_token`` (required to make API calls).

Scopes
======

Select scopes your app needs (see :doc:`scopes </concepts/scopes>` doc).

JWT algorithm
=============

RS256


Website URL
===========

Users have access to this link if they want to know more about your application

Terms URL
=========

Users have access to this link to see your end-user license agreement (EULA).

Logo
====

Your app logo. Users see it next to your app name

Redirect URIs
=============

List of authorized redirect URIs

After allowing your app to access their data, users will be redirected to your app on one of these URIs.

.. tip::

    For security reasons, avoid using locals URL such as *localhost*, *127.0.0.1*, *192.168.x.x*, etc.

Post Logout URIs
=================

List of authorized Post Logout URIs
Useful only if you want to implement an SSO logout.

.. seealso::

    See also :doc:`Authentication documentation </guide/authentication_bimdata_connect>`