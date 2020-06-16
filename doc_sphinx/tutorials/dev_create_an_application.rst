:produit: dev

=========================
Create your application
=========================

.. 
    excerpt
        How-To create your application on BIMData Connect
    endexcerpt

How-To create your application on BIMData Connect
====================================================

* Create an account on the |bimdata_connect| website. 
* After the login step, go to "Manage your application" screen and fill the form to Create an Application.
* Choose a *Name* for your application. let's type **"Wonderful app"** in the field *Name*.
All the fields may be edited later.

These settings allow your app to communicate using a unique Token Access.
Other choices are useful to manage the access rights for every API call.

.. tip::

   Your user has no access to what your application created. To grant access to your user see :doc:`how-to share data with your app <api_share_data_app_platform>`


.. image:: /_images/cookbook/BIMdata_create_application.png
   :scale: 70 %
   :alt: Create your application
   :align: right

You created your first application.

You will see 2 new pieces of information:

* the Client ID 
* the Client Secret


This Client ID and Client Secret are mandatory to build your application.

.. seealso::

    See also :doc:`Authentication documentation </guide/authentication_bimdata_connect>`



Response Type
==============

See the two Types of Auth to learn more about the Response Type.

In the field *Redirect URIs*, set at least the value ``http://localhost``: for now, you want your brand new application to receive any response.

Fields description
====================

Name
------

* You can choose whatever you want. 
* The name is displayed to users when requesting permissions and in their application list.

Scopes
--------

* Select scopes your app needs
* `See the Scopes documentation content <../guide/concepts/scopes.html>`_ to learn more.

Redirect URIs
--------------

* List of authorized redirect URIs.
* After allowing your app to access their data, users will be redirected to your app on one of these URIs.
* By default, the redirect URI is: ``http://localhost:8080/oidc-callback``

.. warning::

    For security reasons, avoid using locals URL such as ``localhost``, ``127.0.0.1``, ``192.168.x.x``, *etc.* for applications in production.

.. seealso::

    See also our documentation :doc:`about Security </guide/dev_security>`