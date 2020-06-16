========================
3D Viewer Documentation
========================

BIMData Viewer is a 3D Viewer built with Web technologies, you can use is in all your web apps.
On top of that our Viewer is customizable through plug-ins.

Usage of the Viewer is either simply embedded in your web application, or with a custom-tailored plugin adapting to your needs the behavior of the Viewer.

.. raw:: html
   :file: ../_static/viewer.html

Display my Models in the Viewer
================================

:doc:`Getting Started with the 3D Viewer </getting_started/viewer>`

Embed the 3D Viewer in my application
======================================

 * :doc:`How-to embed the Viewer using Vue.js </tutorials/viewer_using_vue_component>`

Customize the 3D Viewer
=======================

BIMData provides a 3D Viewer with which you can interact with Javascript.
The Viewer is built with VueJS framework, the architecture of the Viewer is using components, and built-on XeoKit.

 * :doc:`How-to customize the Viewer to your design </tutorials/using_custom_viewer>`

Extend the 3D Viewer
====================

 * :doc:`How-to create a Viewer plugin </tutorials/viewer_create_plugin>`

* Learn about the :doc:`Viewer's events <events>`
* Learn all the :doc:`utils and helper methods <utils>`
* Learn about the :doc:`modal manager <modal_manager>`
* Learn how-to :doc:`make a custom icon for your plugin <custom_plugin_icon>`
* Learn about :doc:`async plugins <async_plugins>`

.. tip::

    Looking for the BIMData Viewer SDK?
    https://github.com/bimdata/bimdata-viewer-sdk

 * :doc:`How-to use the SDK to create a plugin </tutorials/viewer_sdk>`




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

    ../tutorials/viewer_create_plugin
    async_plugins
    custom_plugin_icon
    modal_manager
    ../tutorials/using_custom_viewer
    ../tutorials/viewer_using_vue_component
    ../tutorials/viewer_sdk
    events
    utils

.. _check the WebGL support: https://get.webgl.org
.. _WebGL-enabled browsers: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
.. _ECMAScript 2015 support: https://kangax.github.io/compat-table/es6
