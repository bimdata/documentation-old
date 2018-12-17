.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/index.rst

=======================
Viewer
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.

Guide
=================

* `Including the Viewer in your app`_
* Javascript API: `get your model into the Viewer`_


Usage examples
===============

 * How-to: `doors filtering`_


Example of the Viewer
==========================

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

.. raw:: html
   :file: ../_static/simple_viewer.html


Reference
================

* `JS methods of the viewer`_


.. _get your model into the Viewer: viewer/get_model_from_cloud.html
.. _Including the Viewer in your app: ../viewer/include_viewer.html
.. _doors filtering: ../viewer/example_doors.html
.. _zoom in the model and focus on an element: ../viewer/zoom_in_the_model.html
.. _JS methods of the viewer: ../viewer/parameters.html
