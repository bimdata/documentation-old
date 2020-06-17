========================
3D Viewer Documentation
========================

BIMData Viewer is a 3D Viewer built with Web technologies, you can use is in all your web apps.
On top of that our Viewer is customizable through plug-ins.

Usage of the Viewer is either simply embedded in your web application, or with a custom-tailored plugin adapting to your needs the behavior of the Viewer.

.. image:: /_images/viewer/viewer_zoom.gif
    :align: center
    :scale: 100%
    :alt: Screenshot of the main view of the BIMData's Viewer


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

 * How-to :doc:`customize the Viewer to your design </tutorials/using_custom_viewer>`
 * How-to :doc:`work with annotations <add_annotations>`
 * How-to :doc:`create and delete Sections planes <create_section_planes>`
 * How-to :doc:`add context commands to the Right-click Menu. <customize_context_commands>`
 * How-to :doc:`customize keyboard shortuts <customize_keyboard_shortcuts>`

.. raw:: html
   :file: ../_static/viewer.html

Extend the 3D Viewer
====================

* Learn how-to :doc:`create a Viewer plugin using VueJS </tutorials/viewer_create_plugin>`
* How-to use :doc:`the SDK to create a plugin </tutorials/viewer_sdk>`

* Learn about the :doc:`Modal Manager <modal_manager>` to display data in modals
* Learn how-to :doc:`make a custom icon for your plugin <custom_plugin_icon>`
* Learn about making your :doc:`plugins asynchronous <async_plugins>`

* See useful :doc:`programming Shortcuts with $ <programming_shortcuts>`
* Read the :doc:`Viewer's events reference <events>` 
* See :doc:`all the helpers<utils>` in the reference

.. tip::

    Looking for the BIMData Viewer SDK?
    https://github.com/bimdata/bimdata-viewer-sdk


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
    programming_shortcuts
    add_annotations
    create_section_planes
    customize_context_commands
    customize_keyboard_shortcuts

.. _check the WebGL support: https://get.webgl.org
.. _WebGL-enabled browsers: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
.. _ECMAScript 2015 support: https://kangax.github.io/compat-table/es6
