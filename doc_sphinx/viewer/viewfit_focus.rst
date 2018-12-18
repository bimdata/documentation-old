=================================
Example: using the viewFit focus
=================================

BIMData provides a 3D Viewer with which you can interact with Javascript.

In this example, you want to focus on a given element, and load the Viewer with that focus done.
You will need to obtain the UUID of the element you want to focus on, before this example.

The script has 3 parts:
 * you get the model from the cloud
 * you get the Element you want to set the focus on
 * when you load the Viewer, display the Element's properties

Get the model from the cloud
------------------------------

This part is covered by the Recipe "`How-to get the model from the cloud`_"
In this recipe, it's assumed that you have the IFC's id.


Get the element you want to set the focus on
------------------------------------------------

To follow best practices of JS developement, you declare the elements and the currentElement variables.

.. code-block:: javascript

      var elements = null;
      var currentElement = null;


For this example, you have previously get the UUID of your element.
To get an element, `see the Viewer methods available`_.

.. code-block:: javascript

      // This is the unique ID of the element whose properties we want to display.
      var element_uuid = "1XtCE$bZn2XwBDa8za6_lj";


Then you write a function that changes the viewFit of the Viewer, making your element the center of the current view.
Note that you build the fullUUID by concatening the IFC's id and the UUID itself.

.. code-block:: javascript
      
      /* Selects an object by its UUID, and outputs its properties in the console. */
      function showObjectByUUID(uuid, showProperties){
        var fullUUID = `${ifcId}#${uuid}`;
        currentElement = elements[fullUUID];
        // Change the element's color
        viewer.setColor(fullUUID, [0.2, 0.5, 0.5])
        viewer.viewFit(fullUUID)
      }


Display the Element's properties
----------------------------------

It's now time to use your function. When the Viewer is loading, the viewFit is set to the chosen element. 

.. code-block:: javascript

      // When the viewer fully loaded the model, display our element's property
      viewer.on('viewer-load', function(e) {
          showObjectByUUID(element_uuid, false);
      });


.. raw:: html
   :file: ../_static/st_viewfit_focus.html

.. _see the Viewer methods available: ../viewer/parameters.html
.. _How-to get the model from the cloud: ../viewer/get_model_from_cloud.rst