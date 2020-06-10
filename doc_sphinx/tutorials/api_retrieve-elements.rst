================================
Retrieve elements of your model
================================

.. 
    excerpt
        How-to retrieve elements of your model through the API
    endexcerpt

.. note:: 

    This tutorial is about how-to retrieve elements of your model through the API


    * Topics: application, API, routes, elements
    * Pre-requisites: BIMData Connect account, REST API knowledge, IFC file ready to upload
    * Goal of this tutorial: learn about the common API usage
    * 4 steps

.. highlight:: python
   :linenothreshold: 5

The BIMData Platform allows you to get any information on your model. In this tutorial, you learn how to retrieve elements of your model.
In this tutorial, we use the *client_credential* type of authentication, that is available when you have an application.
Follow the steps and learn how to query your model through our API.

Step 1. Get your token
========================

To get an Access Token, you first `create an application`_ named "Windows retriever".
Then follow `the procedure described on the dedicated page to get your Access Token`_.
You are now ready to use the API.

Step 2. Set up your project
===============================

Once your app exists and you have your Access Token, you can use the API.
Begin with the creation of a Cloud (`What's a cloud?`_), in which you create a Project (`What's a project?`_).
In the script below, there is an example of the creation of a project in your Cloud through API, so you can have a ``projectId``.
First, define a name to create your first Cloud. Post this ``name`` on |api_url|/cloud using your Access Token. 
Then use the ``cloudId`` to create your first Project.

.. code-block:: python

    import requests

    #previous step gave you an access_token
    #prepare headers and cloud_name for POST request
    headers = {
        'authorization': 'Bearer '+ access_token,
    }
    cloud_name = {
        'name': 'Windows retrieval'
    }
    response = requests.post(f'|api_url|/cloud', data=cloud_name, headers=headers)
    assert response.status_code == 201

    cloud_id = response.json().get('id')
    response = requests.post(f'|api_url|/cloud/{cloud_id}/project',  headers=headers)
    assert response.status_code == 201

    project_id = response.json().get('id')

Let's upload your IFC model!

Step 3. Upload your IFC
============================

The API let you upload your IFC file. In this tutorial, you can use this IFC file: `Download the Cassiopea IFC file`_

Use the API to upload
-------------------------

Use the ``/cloud/{cloud_pk}/project/{project_pk}/document`` route to upload your file.
The `documentation for createDocument()`_ is available on our API Reference page.

.. code-block:: python

    import requests

    #prepare headers and payload for POST request
    headers = {
        'authorization': 'Bearer '+ access_token,
    }
    payload = {
        'name': 'My lovely IFC'
    }
    my_ifc_to_upload = {'file': open('/path/to/XXX.ifc', 'rb')}

    #previous script gives you the cloud_id and the project_id
    url = f'|api_url|/cloud/{cloud_id}/project/{project_id}/document'
    response = requests.post(url, data=payload, files=my_ifc_to_upload, headers=headers)
    assert response.status_code == 201

    my_ifc_id = response.json().get('ifc_id')


Follow the upload process
---------------------------

During the upload, you must query the server to get information about the upload process, see `the IFC documentation page`_ about the available information.
The server detects IFC format and you can get information about your file using the API: |api_url|/doc#/ifc/getIfc

.. note::
    The IFC document provided in this tutorial takes approximatively 10 seconds to be processed.\nUsually, the processing time could be very different depending on the IFC file.


.. code-block:: python

    import time
    import requests

    ready = False

    while not ready:
        url = f'|api_url|/cloud/{cloud_id}/project/{project_id}/ifc/{my_ifc_id}'
        response = requests.get(url, headers=headers)
        assert response.status_code == 200

        status = response.json().get('status')

        if('C' == status):
            ready = True
            #your IFC is ready to query
        else:
            #print('not ready yet')
            time.sleep(1)


When the status is *C* meaning Complete, your IFC document is uploaded and processed.
Let's use the BIMData API to query your model!

Step 4. Retrieve windows
===========================

In this tutorial, you want *all the windows of the building* described in your IFC.

Retrieve elements
------------------

The route is: `/cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element`

As listed `on the documentation page for getElements()`_:
the mandatory parameters are:

 * *cloud_pk* string
 * *ifc_pk* string
 * *project_pk* string

Use filters
-------------

In addition, you can filter by:
 * *type* string
 * *classification* string
 * *classification__notation* string

To retrieve only windows, the accurate filter is *type*: **IfcWindow**.
You get a list of windows, all the windows of your model.

.. code-block:: python

    import requests
    # This script requires an IFC document uploaded

    my_filter = {
        'type': 'IfcWindow'
    }
    url = f'|api_url|/cloud/{cloud_id}/project/{project_id}/document/{my_ifc_id}'
    response = requests.get(url, data=my_filter, headers=headers)
    assert response.status_code == 200

    all_windows = response.json()
    #all_windows are available in this var for your next scripts

With the filters, every IFC element can be retrieved. 
You can retrieve any element in the collection provided in the API.

.. seealso::

    For more see :doc:`the API documentation </getting_started/api>`

.. _create an application: ../tutorials/dev_create_an_application.html
.. _the procedure described on the dedicated page to get your Access Token: ../tutorials/dev_get_access_token.html
.. _What's a cloud?: ../guide/concepts/cloud.html
.. _What's a project?: ../guide/concepts/projects.html
.. _Download Cassiopea IFC: https://drive.google.com/file/d/1njhweVCFvDNl8Gy3B1HxAolcfExt0Tg-/view?usp=sharing
.. _documentation for createDocument(): ../api/index.html#createDocument
.. _the IFC documentation page: ../guide/concepts/ifc.html
.. _on the documentation page for getElements(): ../api/index.html#getElements