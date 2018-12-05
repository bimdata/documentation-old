.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/example_doors.rst

===============================
Example: usage of the Viewer
===============================

BIMData provides a 3D Viewer with which you can interact with Javascript.

In this example, you want to check if your doors let the disabled person access to the building.
To evaluate the number of doors that are ok or not ok, you will display all the doors of the model with a color-code according to the minimal width.

The script has 3 parts:
 * you get the model from the cloud
 * the Viewer load the model and you get all doors
 * you hide everything, first then you set a color and show only the doors.

Get the model from the cloud
------------------------------

This part is covered by the Recipe "`How-to get the model from the cloud`_"

Get all the doors
------------------

Using the `ifcApi` you retrieve the doors the element `IfcDoor`, the getElements() methods could take an argument to filter by IFC element.
Then you enlist the doors in two separate lists, based on their width: 

Retrieve the whole script on `our Codepen`_.


Color doors
--------------------------------------------

In this example, you first set all elements as *unpickable*, and you `ghost()` them. Then you `unghost()` and set *pickable* again only the doors elements.
Since you have the doors list, you set the color of the elements related to their width.


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


.. _How-to get the model from the cloud: ../viewer/get_model_from_cloud.html
.. _our Codepen: https://codepen.io/bimdata