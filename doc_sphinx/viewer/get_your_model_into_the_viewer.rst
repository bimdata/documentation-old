.... note:: WIP

    This page is not finished yet.


=====================================
How-to get your model into the Viewer
=====================================

@WIP

Include the Viewer as specified in the  :doc:`Include viewer recipe </viewer/include_viewer>`, then, you will use the BIMData API.

Load the Javascript API
========================

To be able to use the API from the same script than your Viewer, include the API by using this line in your HTML file.
This will include the ``bimdata.ApiClient`` you will use to make your API calls.

.. code-block:: html

    <script type="text/javascript" src="https://unpkg.com/@bimdata/bimdata-api-client/dist/javascript-api-client.min.js"><!-- API call --></script>


What info do you will get?
=================================

The following informations will be obtained:

 * cloud ID, project ID and IFC ID
 * the Access Token as a string


Using the API
===============

Create an instance of the API client. You will store it, in this example, in the ``defaultClient`` var.

.. code-block:: javascript

        var defaultClient = bimdata.ApiClient.instance;

Then, you will use the API client to get the Bearer object, and you Access Token to get your API Key (see the code):


.. code-block:: javascript

        defaultClient.basePath = 'https://api.bimdata.io';
        // Configure API key authorization: Bearer
        var Bearer = defaultClient.authentications['Bearer'];
        Bearer.apiKey = 'Bearer ' + accessToken;


Now, you are able to retrieve the Model from your cloud.
