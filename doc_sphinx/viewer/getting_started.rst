===============================
Getting started with the Viewer
===============================

.. 
    excerpt
        Getting Started with the Viewer
    endexcerpt


.. image:: /_images/viewer/BIMdata_viewer_small.png
   :scale: 100 %
   :alt: Viewer screenshot
   :align: center

Include the Viewer
=======================

With this code in your HTML page, you load a Viewer woth our Demo Model.

.. substitution-code-block:: html

    <!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <head>
    </head>
    <body>
    <div id="embed" style="width: 100%; height: 100vh;"></div>
    <script src="|cdn_url|/js/bimdata-viewer-embed.js"></script>
    <!--the viewer itself -->
    <script type="text/javascript"
        src="https://unpkg.com/@bimdata/bimdata-api-client/dist/javascript-api-client.min.js"></script><!-- API call -->
    <script>
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
    </script>
    </body>
    </html>


Minimal Viewer inclusion
=========================

With this code in your HTML page, you load an empty Viewer.

.. substitution-code-block:: html

    <!DOCTYPE html
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <head>
    </head>
    <body>
    <div id="embed" style="width: 100%; height: 100vh;"></div>
    <script src="|cdn_url|/js/bimdata-viewer-embed.js"></script><!--the viewer itself-- >
    <div id="embed" style="width: 100%; height: 100vh;" ></div>
    <script>
        var viewer = new BIMDataViewer('embed');
    </script>
    </body>
    </html>


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