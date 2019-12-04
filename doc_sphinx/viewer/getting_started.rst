================================
Getting started with the Viewer
================================


Using the Viewer Embedded
==========================

Embed with VueJS
----------------

You can embed the Viewer in your web application using VueJS like a Vue Component.

➤ :doc:`See how-to customize the Viewer display <using_custom_viewer>`.


Embed Viewer without VueJS
----------------------------


.. code-block:: html
   :linenos:
   :caption: main.js

    <!DOCTYPE html>
    <html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>BIMData - CJS Example</title>
        <script src="https://unpkg.com/@bimdata/viewer@0.3.2/dist/bimdata-viewer.min.js" charset="utf-8"></script>
    </head>
    <body>
        <div style="height: 95vh">
        <div id="app"></div>
        </div>
        <script>
        const cfg = {
            cloudId: 88,
            projectId: 100,
            ifcIds: [175],
            bcf:false
        }
        const accessToken = 'DEMO_TOKEN';
        const {viewer, store, eventHub, setAccessToken} = initBIMDataViewer('app', accessToken, cfg);
        </script>
    </body>



.. tip::

    Define in your CSS the minimal size of the Viewer container. The Viewer cannot fill its parent element.


Using a Custom Viewer
=======================

When you need to implement a custom behavior for the Viewer, you create a plug-in.

➤ :doc:`See how-to customize the Viewer's behavior to your needs <create_viewer_plugin>`.

Examples 
------------

* Connect the Viewer with your system to link the 2D map user's actions on the 3D Viewer rendering



