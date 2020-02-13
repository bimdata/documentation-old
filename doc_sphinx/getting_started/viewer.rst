================================
Getting started with the Viewer
================================

..
    excerpt
        The Viewer is a WebGL-based Viewer that you can include in your web apps.
    endexcerpt

.. contents:: Table of Contents
   :depth: 2

Using the Viewer Embedded
==========================


Embed with Vue.js
------------------

You can embed the Viewer in your web application using Vue.js like a Vue Component.

➤ :doc:`See how-to embed the Viewer using Vue.js </tutorials/viewer_using_vue_component>`.


Embed Viewer without Vue.js
----------------------------

If you are not using Vue.js, you can embed the Viewer with a ``<script>`` tag.


See below how-to embed the Viewer in your HTML:


.. code-block:: html
   :linenos:
   :caption: Complete content of the ``index.html`` file

    <!DOCTYPE html>
    <html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>BIMData - CJS Example</title>
        <script src="https://unpkg.com/@bimdata/viewer/dist/bimdata-viewer.min.js" charset="utf-8"></script>
    </head>
    <body>
        <div style="height: 100vh">
            <div id="app"></div>
        </div>
        <script>
          const cfg = {
            cloudId: 88,
            projectId: 100,
            ifcIds: [175],
            bimdataPlugins: {
              bcf:false
            }
          }
          const accessToken = 'DEMO_TOKEN';
          const {viewer, store, eventHub, setAccessToken} = initBIMDataViewer('app', accessToken, cfg);
        </script>
    </body>
    </html>


.. warning::

    Define in your CSS the size of the Viewer container. The Viewer cannot automatically fill its parent element.


Using a Custom Viewer
=======================

When you need to implement custom behavior for the Viewer, you create a plugin.

➤ :doc:`See how-to customize the Viewer's behavior to your needs </tutorials/viewer_create_plugin>`.

By example, you could connect the Viewer with your system to link the 2D map user's actions on the 3D Viewer rendering.



