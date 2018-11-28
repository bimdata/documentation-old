=======================
Viewer
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.


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

.. raw:: html
   :file: ../_static/simple_viewer.html


Usage
-----------

* `Including the Viewer in your app`_


Examples
------------

 * How-to: `doors filtering`_



.. _Including the Viewer in your app: include_viewer
.. _doors filtering: example_doors