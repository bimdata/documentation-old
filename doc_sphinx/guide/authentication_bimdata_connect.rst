===================================
Authentication with BIMData Connect
===================================

.. 
    excerpt
        BIMData Connect handles sign-in and log in for your app.
    endexcerpt

The OpenID Connect used by the BIMData Connect, our authentication system, is built on the shoulders of oAuth2.0. 

BIMData Connect handles the sign-in, the login and authentication processes of your application users. 
You can focus on creating and building your application.
The user's browser is redirect to the Sign-In page by the Web Application.

The Sign-In page is on the BIMData Connect server. The BIMData Connect provides to the user's browser an Access Token.
Then the user's browser could send requests to the Web Application sending the Access Token.
The type of authentication is defined during the creation of the application.

.. image:: /_images/guide/BIMdata_connect_diagram_colors.jpg
   :scale: 80 %
   :alt: BIMData Connect handles sign-in and log in for your app
   :align: center

*BIMData Connect handles sign-in and log in for your app*

Get your Access Token
=====================

.. WARNING::
    Requirement: you must have an application, see `Create an application process`_.

Follow the procedure described in `Authentication by client credential`_

.. image:: /_images/guide/auth_flow_diagram_colors.jpg
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

.. IMPORTANT:: titre
    You cannot access as a user, therefore you cannot:

    * do any impersonation
    * manager fine granularity with access rights


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

The three types are three different mechanisms to aks for user's permissions.

Authorization code flow
-----------------------

This is the most common flow. 
Behave as a user even without the user actually using the application, directly inherited from OAuth (ie: cron, asynchronous data processing)
* You can proxy your users through your back-end to  between their browser and BIMData API
* You can forward the Access Token to the browser and let the browser directly call the BIMData API. 
It this case, you need to implement a way to refresh the Access Token when it expires.

.. highlights::
    Example: enrichment of your app's data with your own dataset.

Implicit flow
-------------

Usage of the access enabled by the user currently connected into the application.
`Implicit flow` is the way when you don't need a back-end software. Everything is done in the user's browser. 
It retrieves the access_token and can use it as you want. But when the token expires, you need the user to refresh it.

.. highlights::

    Example: get the Access Token by the browser to use it directly after getting it.

.. highlights::
    Example2: reporting into the application of the user's actions


Hybrid flow
-----------

This option combines the previous two options: you can make some reporting and actions as a user.

.. highlights::
    Example: The BIMData platform uses this auth option.



.. _Create an application process: ../cookbook/create_an_application.html
.. _Authentication by client credential: ../cookbook/get_access_token.html
.. _Your Access Token: ../cookbook/get_access_token.html