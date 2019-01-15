.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/index.rst

=======================
Viewer Documentation
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.

Guide
=================

* `Including the Viewer in your app`_


Cookbook
===============

Usage examples of the Viewer:

 * How-to: `init the Viewer`_
 * How-to: `doors filtering`_
 * How-to: `use the viewFit focus`_



Reference
================

* `Javascript methods of the Viewer`_


Example of the Viewer
==========================

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


Requirements
=================

Only `WebGL-enabled browsers`_ are supported:

* Firefox
* Chrome
* Edge
* Safari 11 or later

.. note::

    `Test the WebGL support`_ of your browser.

Recommended
------------

For best performance, use the latest versions of modern browsers: Firefox, Chrome, Edge or Safari.
In addition to that, we recommend:

* 4 GB RAM (1GB for the system, 1GB for the browser and 2GB for the Viewer)
* Javascript and built-in hardware acceleration enabled
* Modern browser with `ECMAScript 2015 support`_

.. _Including the Viewer in your app: ../viewer/include_viewer.html
.. _init the Viewer: ../viewer/init_viewer.html
.. _doors filtering: ../viewer/example_doors.html
.. _zoom in the model and focus on an element: ../viewer/zoom_in_the_model.html
.. _Javascript methods of the Viewer: ../viewer/parameters.html
.. _use the viewFit focus: ../viewer/viewfit_focus.html
.. _Test the WebGL support: https://get.webgl.org
.. _WebGL-enabled browsers: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
.. _ECMAScript 2015 support: https://kangax.github.io/compat-table/es6
