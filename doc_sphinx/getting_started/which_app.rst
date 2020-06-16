==============================
Which app will you create?
==============================

..
    excerpt
        Application with a backend, or single page
    endexcerpt

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