================================
Include the Viewer in your app
================================

To support the Viewer you will need a `<div>` element, with an id attribute, and 3 scripts:

* The JS viewer to embed with the `<script>` tag
* The API Javascript client, for API calls, to embed with the script tag
* Your own JS script: in this documentation, this part will be directly in the HTML `<script>` tag

  .. code-block:: html

    <script src="https://cdn-beta.bimdata.io/js/bimdata-viewer-embed.js" ><!--the viewer itself --></script>
    <script type="text/javascript" src="https://unpkg.com/@bimdata/bimdata-api-client/dist/javascript-api-client.min.js"><!-- API call --></script>
    <script>


The <div> element
==================

You `<div>` is simply styled by taking the whole screen width and height.
An ID will ensure the easy access in Javascript scripts.

  .. code-block:: html

    <div id="embed" style="width: 100%; height: 100vh;" ></div>

JS Viewer script
=================

The Viewer is based on XeoGL Engine and... @TODO

.. http://xeogl.org/

Object BIMDataViewer


JS API client script
====================

This client will help you making API calls to get your data. 
You will need your Access Token (see the Cookbook Recipe How-to get your Access Token) to get your authentication.

.. code-block:: javascript

      defaultClient.basePath = 'https://api-beta.bimdata.io';
      // Configure API key authorization: Bearer
      var Bearer = defaultClient.authentications['Bearer'];
      Bearer.apiKey = 'Bearer ' + accessToken;

Your own Javascript script
==========================

You will use the bimdata namespace

bimdata.ApiClient
bimdata.IfcApi