.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/index.rst

=======================
Viewer Documentation
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.

:doc:`Getting started <getting_started>`

Guide
=================

* :doc:`Include the Viewer in your app <include_viewer>`


Cookbook
===============

Usage examples of the Viewer:

 * How-to: :doc:`init the Viewer <init_viewer>`
 * How-to: :doc:`doors filtering <example_doors>`
 * How-to: :doc:`use the viewFit focus <viewfit_focus>`



Reference
================

* :doc:`Javascript methods of the Viewer <parameters>`


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

.. _Test the WebGL support: https://get.webgl.org
.. _WebGL-enabled browsers: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
.. _ECMAScript 2015 support: https://kangax.github.io/compat-table/es6

.. toctree::
    :hidden:
    
    getting_started
    include_viewer
    example_doors
    init_viewer
    get_your_model_into_the_viewer
    parameters
    viewfit_focus
    zoom_in_the_model
