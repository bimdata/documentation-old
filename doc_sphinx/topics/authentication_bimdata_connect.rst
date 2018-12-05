===================================
Authentication with BIMData Connect
===================================

The OpenID Connect used by the BIMData Connect, our authentication system, is built on the shoulders of oAuth2.0. BIMData Connect handles the sign-in, the login and authentication processes of your application users. You can focus on creating and building your application.
BIMData Connect handles sign-in and log in for your app

.. image:: /_images/topics/BIMdata_connect_diagram_colors.jpg
   :scale: 80 %
   :alt: BIMData Connect handles sign-in and log in for your app
   :align: center

*BIMData Connect handles sign-in and log in for your app*

Get your Access Token
=====================

.. WARNING::
    Requirement: you must have an application, see `Create an application process`_.

Follow the procedure described in `Authentication by client credential`_

.. image:: /_images/topics/auth_flow_diagram_colors.jpg
   :scale: 100 %
   :alt: Authentication flow
   :align: center


*Authentication flow*

Use your Access Token
=====================

There are two possible ways to authenticate depending on your application architecture design.
You can either access as an application and benefit from authentication capacities
or use a user-behavior authentication.

When use an app auth?
=====================

The benefits
------------

    **Simple to use**

    No user means no credentials to manage nor complex workflow, it's simpler to access via the application.

    **Pluggable**

    You can subscribe to events and use webhooks.

    **Cloud by cloud**

    `Your Access Token`_ will let you access to one cloud information and data at the time.

Use it when you need to have a scheduled response to an event and launch a script depending on this response.

.. IMPORTANT::
    You cannot access as a user, therefore you cannot:

        do any impersonation
        manager fine granularity with access rights


When use a user impersonation?
==============================


The benefits
-------------


User's name as author
^^^^^^^^^^^^^^^^^^^^^^^

Emulating the user's actions enables you to act in the name of the user. Creating content with impersonation writes the user's name in the creator's name of this content.


Sharing the authoring
^^^^^^^^^^^^^^^^^^^^^^

Your script can modify data created by the user and amend it.


Let BIMData handle the complexity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The credentials complexity is handled by the BIMData Connect authentication server. This option is compliant with the user's credentials.

Use it when you need to access the user's log, such as user's history, and report actions.

There are three types of user auth, detailed beneath:

* Authorization code flow
* Implicit flow
* Hybrid flow

Type of user auth detailed
===========================

The three types serve different purposes.



Authorization code flow
-----------------------

Behave as a user even without the user actually using the application.
Example: Useful when you try to enrich the data of your app with your own dataset.


Implicit flow
-------------

Usage of the access enabled by the user currently connected into the application.
Example: get the Access Token by the browser to use it directly after getting it.
Example2: reporting into the application of the user's actions


Hybrid flow
-----------

This option combines the previous two options: you can make some reporting and actions as a user.
Example: The BIMData platform uses this auth option.



.. _Create an application process: ../cookbook/create_an_application
.. _Authentication by client credential: ../cookbook/get_access_token
.. _Your Access Token: ../cookbook/get_access_token