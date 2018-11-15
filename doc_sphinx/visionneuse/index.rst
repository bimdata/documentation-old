=======================
Viewer
=======================

Example of the Viewer:
-------------------------

.. code-block:: javascript

      var accessToken = 'DEMO_TOKEN';
      var cloudId = 88;
      var projectId = 100;
      var ifcId = 175;
      var defaultClient = bimdata.ApiClient.instance;
      
      defaultClient.basePath = 'https://api-beta.bimdata.io';
      // Configure API key authorization: Bearer
      var Bearer = defaultClient.authentications['Bearer'];
      Bearer.apiKey = 'Bearer ' + accessToken;
      
      var viewer = new BIMDataViewer('embed', {
        accessToken: accessToken,
        cloudId: cloudId,
        projectId: projectId,
        ifcId: ifcId
      });
      
      // Wait the viewer to finish loading
      viewer.on('viewer-load', function(e) {
        // Hide all elements of the model
        var ifcApi = new bimdata.IfcApi();
        // Get all doors by filtering with specifying a type
        ifcApi.getElements(cloudId, ifcId, projectId, {type: 'IfcDoor'}).then(function(doors) {
          // Ghost all elements
          viewer.ghost();
          viewer.setUnpickable();
          ....
          viewer.unghost(doorsUuidList);
          viewer.setPickable(doorsUuidList);
          // Color in green doors that are adapted to disabled persons and unghost doors
          viewer.setColor(adaptedDoorsUuidList, [0, 1, 0]);
          // Color in red doors that are not adapted to disabled persons and unghost doors
          viewer.setColor(unadaptedDoorsUuidList, [1, 0, 0]);
        }, console.error);
      });


.. raw:: html
   :file: ../_static/st_iframe.html
