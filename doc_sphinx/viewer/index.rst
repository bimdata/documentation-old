.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/index.rst

=======================
Viewer Documentation
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.
The Viewer is built with VueJS framework, and the architecture of the Viewer is with components.

Guide
======


.. tip::

    Define in your CSS the minimal size of the Viewer container. The Viewer cannot fill its parent element.

Embedded
---------

 * With VueJS
 * Without VueJS

Custom Viewer
----------------

Behavior
Plugin
Connect the Viewer with your system (ie: 2D map acting on the 3D viewer)

Tutorials
==========

 * How-to make a Viewer plug-in

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