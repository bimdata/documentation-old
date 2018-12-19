.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/index.rst

=======================
Viewer Documentation
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.

Guide
=================

* `Including the Viewer in your app`_
* Javascript API: `get your model into the Viewer`_


Cookbook
===============

Usage examples of the Viewer:

 * How-to: `doors filtering`_
 * How-to: `use the viewFit focus`_



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


Reference
================

* `JS methods of the viewer`_


.. _get your model into the Viewer: ../viewer/get_model_from_cloud.html
.. _Including the Viewer in your app: ../viewer/include_viewer.html
.. _doors filtering: ../viewer/example_doors.html
.. _zoom in the model and focus on an element: ../viewer/zoom_in_the_model.html
.. _JS methods of the viewer: ../viewer/parameters.html
