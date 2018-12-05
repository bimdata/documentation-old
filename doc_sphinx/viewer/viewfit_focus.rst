.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/viewfit_focus.rst

==================
Viewer viewfit
==================

.. code-block:: javascript

      var ifcId = 175;
      
      var viewer = new BIMDataViewer('embed', {
        accessToken: 'DEMO_TOKEN', 
        cloudId: 88,
        projectId: 100,
        ifcId: ifcId
      });

      var elements = null;
      var currentElement = null;
      
      // This is the unique ID of the element whose properties we want to display.
      var element_uuid = "1XtCE$bZn2XwBDa8za6_lj";
      
      /* Selects an object by its UUID, and outputs its properties in the console. */
      function showObjectByUUID(uuid, showProperties){
        var fullUUID = `${ifcId}#${uuid}`;
        currentElement = elements[fullUUID];
        console.log(currentElement);
        // viewer.select(fullUUID);
        // Change the element's color
        viewer.setColor(fullUUID, [0.2, 0.5, 0.5])
        viewer.viewFit(fullUUID)
      }
      
      // When the viewer fully loaded the model, display our element's property
      viewer.on('viewer-load', function(e) {
      elements = viewer.getElementsInfo();
      showObjectByUUID(element_uuid, false);
      });