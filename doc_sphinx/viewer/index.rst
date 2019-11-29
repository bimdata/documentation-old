.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/index.rst

=======================
Viewer Documentation
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.
The Viewer is built with VueJS framework, the architecture of the Viewer is using components, and built-on XeoGL, the opensource

Usage of the Viewer is either simply embedded in your web application, or with a custom to your needs plug-in changing the behavior of the Viewer. 

Guide
======

* :doc:`Getting Started with the Viewer </viewer/getting_started>`

Reference
===========

* :doc:`Events and listeners </viewer/listeners>`

Tutorials
==========

 * :doc:`How-to customize the Viewer to your design </viewer/using_custom_viewer>`
 * :doc:`How-to create a Viewer plug-in </viewer/create_viewer_plugin>`

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

.. toctree::
    :hidden:

    getting_started
    create_viewer_plugin
    using_custom_viewer
    listeners

.. _Test the WebGL support: https://get.webgl.org
.. _WebGL-enabled browsers: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
.. _ECMAScript 2015 support: https://kangax.github.io/compat-table/es6