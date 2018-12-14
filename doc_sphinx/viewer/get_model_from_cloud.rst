==========================================================
How-to get your model from your cloud for the Viewer
==========================================================


Include the Viewer as specified in the  `Include viewer recipe`_, then, you will use the BIMData API.

Load the Javascript API
========================

To be able to use the API from the same script than your Viewer, include the API by using this line in your HTML file.
This will include the ``bimdata.ApiClient`` you will use to make your API calls.

.. code-block:: javascript

    <script type="text/javascript" src="https://unpkg.com/@bimdata/bimdata-api-client/dist/javascript-api-client.min.js"><!-- API call --></script>
  
  
What info do you will need?
=================================

The following informations will be needed:

 * cloud ID, project ID and IFC ID
 * the Access Token as a string
 * the Bearer will be 


Using the API
===============

Begin with defining all the variables, for an easier maintenance.

.. code-block:: javascript

    <script>
        var accessToken = 'DEMO_TOKEN';
        var cloudId = 88;
        var projectId = 100;
        var ifcId = 175;

Create an instance of the API client. You will store it, in this example, in the ``defaultClient`` var.

.. code-block:: javascript

        var defaultClient = bimdata.ApiClient.instance;

Then, you will use the API client to get the Bearer object, and you Access Token to get your API Key (see the code):


.. code-block:: javascript
        
        defaultClient.basePath = 'https://api-beta.bimdata.io';
        // Configure API key authorization: Bearer
        var Bearer = defaultClient.authentications['Bearer'];
        Bearer.apiKey = 'Bearer ' + accessToken;
      

Now, you are able to retrieve the Model from your cloud.
Instanciate the BIMDataViewer and pass to it the IDs of your Cloud, your Project and your IFC file to get a Viewer for the Model your IFC describe.

.. code-block:: javascript

        var viewer = new BIMDataViewer('embed', {
            accessToken: accessToken,
            cloudId: cloudId,
            projectId: projectId,
            ifcId: ifcId
        });


.. _Include viewer recipe: viewer/include_viewer.html