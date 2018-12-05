.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/include_viewer.rst

================================
Include the Viewer in your app
================================

To support the Viewer you will need a `<div>` element, with an id attribute, and 3 scripts:

* The JS viewer to embed with the `<script>` tag
* The API Javascript client, for API calls, to embed with the script tag
* Your own JS script: in this documentation, this part will be directly in the HTML `<script>` tag

  .. code-block:: html

    <script src="https://cdn-beta.bimdata.io/js/bimdata-viewer-embed.js" ><!--the viewer itself --></script>
    <script>


The <div> element
==================

You `<div>` is simply styled by taking the whole screen width and height.
An ID will ensure the easy access in Javascript scripts.

  .. code-block:: html

    <div id="embed" style="width: 100%; height: 100vh;" ></div>

JS Viewer script
=================

The Viewer is based on `XeoGL Engine`_, see the `list of the methods of the Viewer`_ to interact with the Viewer.

The Viewer is the object BIMDataViewer. The construction of a new BIMDataViewer expects an HTMLElement or a string (ID of this HTMLElement). 
You will use the <div> ID.


Your own Javascript script
==========================

You can now interact with the Viewer in your script. 

.. _XeoGL Engine: http://xeogl.org/
.. _list of the methods of the Viewer: ../viewer/parameters.html
