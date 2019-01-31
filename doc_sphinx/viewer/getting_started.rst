===============================
Getting started with the Viewer
===============================

.. image:: /_images/viewer/BIMdata_viewer_small.png
   :scale: 100 %
   :alt: Viewer screenshot
   :align: center

Include the Viewer
=======================

With this code in your HTML page, you load an empty Viewer.

.. code-block:: html

    <script src="https://cdn-beta.bimdata.io/js/bimdata-viewer-embed.js"></script><!--the viewer itself-- >
    <div id="embed" style="width: 100%; height: 100vh;" ></div>
    <script>
        var viewer = new BIMDataViewer('embed');
    </script>


Load your model 
================

Replace the Javascript by the following code, and you load a Viewer with your Model.

.. code-block:: javascript

    var myAccessToken = 'DEMO_TOKEN';
    var myCloudId = 88;
    var myProjectId = 100;
    var myIfcId = 175;
    
    var viewer = new BIMDataViewer('embed', {
    accessToken: myAccessToken,
    cloudId: myCloudId,
    projectId: myProjectId,
    ifcId: myIfcId
    });


Customize the Viewer
=====================

See `the available methods`_ to customize the Viewer.

.. _the available methods: ../viewer/parameters.html