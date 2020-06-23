=============================
BIMData's API Introduction
=============================

..
    excerpt
        What is the BIMData API? Learn about it.
    endexcerpt

What is the BIMData API?
========================

BIMData API is composed of five other APIs: an IFC API, a BCF API, a Collaboration API, a Checker API and a SSO API.

.. image:: /_images/guide/api_applications.png
    :align: right
    :scale: 50 %
    :alt: Where are the applications in the BIMData's ecosystem

The IFC API
------------

 * Upload Models
 * Retrieve and update Model's data in real-time

We support the following implementations:

  * IFC Spacial Structure
  * IFC Zones
  * IFC Classifications
  * IFC Systems
  * IFC Layers
  * IFC Properties and PropertySets
  * 3D models `throught glTF format <https://www.khronos.org/gltf/>`_

.. tip::

    For more details, see: :doc:`our IFC Guide <../guide/concepts/ifc>`


The BCF API
------------

 * Create BCF
 * Share BCFs with other services
 * Build a complete automated error management flow
 * We implement the `BCF 2.1 API <https://github.com/buildingSMART/BCF-API>`_ defined by BuildingSMART


The Collaboration API
------------------------

 * Create projects
 * Invite users
 * Manage their rights
 * Share models, data and documents


The Checker API
----------------

 * Validate your Models


The Single Sign-On (SSO) API
-----------------------------

 * Log in on desktop, tablet, mobile
 * Log in all your BIM Services through BIMData Connect: |bimdata_connect|
 * Log in through your own SSO (OpenID Connect or SAMLv2)

.. seealso::
    
    Read about :doc:`the Users Management in API <../guide/dev_users_management>`


First steps with the API
========================

OpenID
---------

BIMData API uses the OpenID Connect protocol (technically very similar to the OAuth2 protocol). 
Any OpenID library you may find online to help you implement the protocol also works with BIMData API


Make API calls
---------------

To make API calls, you must retrieve an Access Token. There are many ways to get one depending on the context or your application.
We'll use the simplest one for this 'Getting Started' and you can find :doc:`the details of all methods in the tutorial dedicated to the Access Token <../tutorials/dev_get_access_token>`.


Create your application 
---------------------------

The first step is to create your application: as described in the :doc:`create your application documentation <../tutorials/dev_create_an_application>`.
For the Getting Started, you want a confidential app.
That means the app is able to keep a secret (a JavaScript app or a mobile app can't because the code, and therefore the secret, is visible by the user)

.. note:: 

    By default, an app has only access to its data. It can't see data from another app or another user. 
    
    For example, your app won't be able to see the data you have put on the BIMData Platform.

.. tip:: 

    You can also do this tutorial with our Postman collections!
        * The full API collection: https://documenter.getpostman.com/view/7460463/SzKTvyVR
        * The BIMData's Examples collection: https://documenter.getpostman.com/view/7460463/SzKbLFKH


Get your Access Token
----------------------

Once you have created your app, you have a *client_id* and a *client_secret*.
You can exchange them for an Access Token through an HTTP call. 

.. seealso::
 
    See :doc:`Get Access Token documentation for further information <../tutorials/dev_get_access_token>`

Once you have the access_token, you can start doing API calls!


Create your Cloud
-------------------

The first thing to do is to create a *Cloud*. A Cloud is a configurable space where projects are created. 
All projects in this Cloud share the Cloud's configuration.

.. seealso::

    `See the **Create Cloud** endpoint in the API Reference <../api/index.html#createCloud>`_

A Cloud just needs a name:

.. prompt:: bash
   :substitutions:

    curl --request POST '|api_url|/cloud' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
    --data '{"name": "My First Cloud"}'

You get a Cloud ID in the response. We need it for our next API call.


Upload your first Model
-------------------------

Once you have your first Cloud, you may want to create your first Project and upload your first Model.
For this tutorial, use a special endpoint that creates a demo Project with our demo Model: `createDemo </api/index.html#createDemo>`_.


.. prompt:: bash
   :substitutions:

    curl --request POST '|api_url|/cloud/YOUR_CLOUD_ID/create-demo' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer YOUR_ACCESS_TOKEN'

You receive back the created Project (its ID).

.. note::
 
    You can also do it with the combination of the endpoints:
       * `createProject <https://developers-staging.bimdata.io/api/index.html#createProject>`_ 
       * and then `createDocument <https://developers-staging.bimdata.io/api/index.html#createDocument>`_


Retrieve our Model
--------------------

Let's retrieve the Model in the demo using `the getIfcs endpoint <https://developers-staging.bimdata.io/api/index.html#getIfcs>`_!


.. prompt:: bash
   :substitutions:

    curl --request GET '|api_url|/cloud/YOUR_CLOUD_ID/project/YOUR_PROJECT_ID/ifc' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer YOUR_ACCESS_TOKEN'


You get an array of the Models in the Project.
Keep the IFC ID, you need it in the next, and it will be the last, call.


Get properties
---------------

Let's get the properties of all the doors of the Model with `the getSimpleElements endpoint <https://developers-staging.bimdata.io/api/index.html#getSimpleElements>`_.

.. prompt:: bash
   :substitutions:

    curl --request GET '|api_url|/cloud/YOUR_CLOUD_ID/project/YOUR_PROJECT_ID/ifc/YOUR_IFC_ID/element/simple?type=IfcDoor' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer YOUR_ACCESS_TOKEN'


And it's done!
-------------------

Hourra: you get all the properties of all the doors of the Model!


.. tip::

    You know the basics our the BIMData API. Go further with the following suggestions:

    * Explore :doc:`the list of all endpoints on the API Reference </api/index>`
    * If you want to :doc:`try the API calls directly from the web, use our API playground </api_playground/index>`.

.. seealso::

    The tutorials in which you find the answers to the questions: 

    * :doc:`How can I share data between my app and BIMData Platform? </tutorials/api_share_data_app_platform>`
    * :doc:`How can I use BIMData Viewer with my uploaded models? </tutorials/api_use_viewer_with_uploaded_models>`
