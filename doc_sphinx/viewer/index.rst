=======================
Viewer
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.

Usage
-----------

* `Including the Viewer in your app`_
* Javascript API: `get your model into the Viewer`_


Examples
------------

 * How-to: `doors filtering`_



Example of the Viewer:
-------------------------

.. code-block:: javascript

      var accessToken = 'DEMO_TOKEN';
      var cloudId = 88;
      var projectId = 100;
      var ifcId = 175;
      
      var viewer = new BIMDataViewer('embed', {
        accessToken: accessToken,
        cloudId: cloudId,
        projectId: projectId,
        ifcId: ifcId
      });

.. raw:: html
   :file: ../_static/simple_viewer.html


.. toctree::
    :hidden:

    include_viewer
    example_doors
    get_model_from_cloud
    viewfit_focus
    parameters


.. _Including the Viewer in your app: include_viewer.html
.. _doors filtering: example_doors.html
.. _get your model into the Viewer: get_model_from_cloud.html