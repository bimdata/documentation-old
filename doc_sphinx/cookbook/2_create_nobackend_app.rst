========================
Create backend-less app
========================

.. 
    excerpt
        How-To create a mobile or tablet application on BIMData Connect
    endexcerpt

.. image:: /_images/cookbook/BIMdata_create_application.png
   :scale: 100 %
   :alt: Create your application
   :align: right

Name
=====

You can chose whatever you want. The name is displayed to users when requesting permissions and in their application list.


Scopes
======

Select scopes your app needs (see :doc:`scopes </concepts/scopes>` doc).


Redirect URIs
=============

List of authorized redirect URIs

After allowing your app to access their data, users will be redirected to your app on one of these URIs.

.. tip::

    For security reasons, avoid using locals URL such as *localhost*, *127.0.0.1*, *192.168.x.x*, etc.

.. seealso::

    See also :doc:`Authentication documentation </guide/authentication_bimdata_connect>`