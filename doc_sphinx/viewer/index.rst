.. meta::
   :github: https://github.com/bimdata/documentation/blob/develop/doc_sphinx/viewer/index.rst

=======================
Viewer Documentation
=======================

BIMData Viewewr is a 3D Viewer built with Web technologies, you can use is in all your web apps.
On top of that our Viewer is customizable through plug-ins.

Guide
======

Usage of the Viewer is either simply embedded in your web application, or with a custom-tailored plugin adapting to your needs the behavior of the Viewer.

* :doc:`Getting Started with the Viewer </getting_started/viewer>`

Reference
===========

* Learn about the :doc:`Viewer's events </viewer/events>`
* Learn all the :doc:`utils and helper methods </viewer/utils>`
* Learn about the :doc:`modal manager </viewer/modal_manager>`
* Learn how-to :doc:`make a custom icon for your plugin </viewer/custom_plugin_icon>`
* Learn about :doc:`async plugins </viewer/async_plugins>`

.. tip::

    BIMData Viewer SDK
    -------------------

    Looking for the SDK?
    https://github.com/bimdata/bimdata-viewer-sdk


Tutorials
==========

BIMData provides a 3D Viewer with which you can interact with Javascript.
The Viewer is built with VueJS framework, the architecture of the Viewer is using components, and built-on XeoKit.

 * :doc:`How-to use the SDK to create a plugin </tutorials/viewer_sdk>`
 * :doc:`How-to customize the Viewer to your design </tutorials/using_custom_viewer>`
 * :doc:`How-to embed the Viewer using Vue.js</tutorials/viewer_using_vue_component>`
 * :doc:`How-to create a Viewer plugin </tutorials/viewer_create_plugin>`

Example of code
=================

.. code-block:: html

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
              bcf: false,
              merge: false,
              allowExport: false
            }
          }
          const accessToken = 'DEMO_TOKEN';
          const { viewer, store, eventHub, setAccessToken } = initBIMDataViewer('app', accessToken, cfg);
        </script>
    </body>
    </html>

.. raw:: html
   :file: ../_static/viewer.html

Requirements
=================

Only `WebGL-enabled browsers`_ are supported:

* Firefox
* Chrome

.. tip::

    On this website, you can `check the WebGL support`_ of your browser.

Recommended
------------

For best performance, use the latest versions of modern browsers: Firefox or Chrome.
In addition to that, we recommend:

* 4 GB RAM (1GB for the system, 1GB for the browser and 2GB for the Viewer)
* Javascript and built-in hardware acceleration enabled

.. toctree::
    :hidden:

    /tutorial/create_viewer_plugin
    async_plugin
    custom_plugin_icon
    modal_manager
    /tutorial/using_custom_viewer
    /tutorial/using_vue_component
    /tutorials/viewer_sdk
    events
    utils

.. _check the WebGL support: https://get.webgl.org
.. _WebGL-enabled browsers: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
.. _ECMAScript 2015 support: https://kangax.github.io/compat-table/es6
