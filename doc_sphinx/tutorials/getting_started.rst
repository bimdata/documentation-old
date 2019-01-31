===============
Getting Started
===============

#. Create a BIMData Connect account
#. Create your app
#. Use the API
    #. `Use your credentials to log in`_
    #. `Create your first cloud and its first project`_
    #. Upload your IFC file in your project
    #. Get all the information pieces from your IFC
#. BONUS: `Include the Viewer on your website`_

Create a BIMData Connect account
===================================

First, you need an account.
Fill the form with your e-mail and name, chose a password and you have your account.

.. image:: /_images/tutorials/BIMdata_connect_create_an_account.png
   :scale: 100 %
   :alt: Fill the form
   :align: center


Create your app
======================

In the BIMData Connect Account Manager screen, go to "Manage your applications" in the Developer area.
There you can create an application.

.. image:: /_images/tutorials/BIMdata_connect_manage_your_app.png
   :scale: 100 %
   :alt: Fill the form
   :align: center

Once your first app is created, you have a Client ID and a Client secret, this will help you with your API credentials.

.. image:: /_images/tutorials/BIMdata_connect_client_ID_client_secret.png
   :scale: 100 %
   :alt: Fill the form
   :align: center


Use the API
======================

Use your credentials to log in
----------------------------------

The Client ID and the Client Secret are the 2 elements you need to `get the Access Token`_ of your app from the Identity Provider. 
You will need this Access Token for every call of the BIMData's API.

Create your first cloud and its first project
-------------------------------------------------

See the `details for the route /cloud/ for the cloud creation`_ and for `the route cloud/{cloud_pk}/project`_ the project creation.

.. code-block:: python

        response = requests.post(f'https://api-staging.bimdata.io/cloud', data=cloud_name, headers=headers)
        cloud_id = response.json().get('id')
        response = requests.post(f'https://api-staging.bimdata.io/cloud/{cloud_id}/project',  headers=headers)



Upload your IFC file in your project
--------------------------------------


.. code-block:: python

        url = f'https://api-staging.bimdata.io/cloud/{cloud_id}/project/{project_id}/document'
        response = requests.post(url, data=payload, files=ifc_path_to_upload, headers=headers)

.. note::

    This is `a step of our Viewer Tutorial`_

Get all the information pieces from your IFC
----------------------------------------------

.. code-block:: python

        url = f'https://api-staging.bimdata.io/cloud/{cloud_id}/project/{project_id}/document/{my_ifc_id}'
        response = requests.get(url, data=my_filter, headers=headers)

.. note:: 

    Many filters are available, `check out the getElements route`_

Include the Viewer
=======================

See the dedicated page `Getting Started with the Viewer`_


.. _Include the Viewer in your website: ../viewer/getting_started.html
.. _get the Access Token: ../cookbook/get_access_token.html
.. _Use your credentials to log in: ../cookbook/get_access_token.html
.. _Create your first cloud and its first project: ../tutorials/retrieve-elements.html#step-2-set-up-your-project
.. _details for the route /cloud/ for the cloud creation: ../redoc/index.html#operation/createCloud
.. _the route cloud/{cloud_pk}/project: https://developers-staging.bimdata.io/redoc/index.html#operation/createProject
.. _a step of our Viewer Tutorial: ../tutorials/retrieve-elements.html#step-3-upload-your-ifc
.. _check out the getElements route: ../redoc/index.html#operation/getElements