=====================
Customize the Viewer
=====================

The BIMData's Viewer is highly customizable to your needs.


Load the Viewer
================

To load the Viewer in your web application, use the ``<script>`` tag with the packaged version:

.. substitution-code-block:: javascript
    
    <script src="https://unpkg.com/@bimdata/viewer@0.3.3/dist/bimdata-viewer.min.js" charset="utf-8"></script>

In your JavaScript:

 * set the data about which IFC model you load
 * then set the options you want


Viewer functionalities
========================

The Viewer is provided with many functionalities by default. Each one can be disabled independantly.
In the cfg Object (see ::doc:`/viewer/getting_started` ), you can disable any plugin by setting it to ``false``:


Each functionality has a default value and could be disabled.


.. list-table:: Viewer functionalities
   :header-rows: 1
   :widths: 10 20 20 40

   * - Name
     - Values 
     - Default value
     - Description
   * - reload
     - Boolean: true/false
     - true
     - ...
   * - model
     - Boolean: true/false
     - true
     - list of the Models loaded
   * - help
     - Boolean: true/false
     - true 
     - Help icon, linked to the [?] keyboard shortcut
   * - section
     - Boolean: true/false
     - true 
     - Section icon
   * - projection
     - Boolean: true/false
     - true 
     - Projection selection icon
   * - selectOptions
     - Boolean: true/false
     - true 
     - ...
   * - structureAndProperties
     - Boolean: true/false
     - true 
     - List structure and properties, in window manager based panels.
   * - bcf
     - Boolean: true/false
     - true 
     - BCF plugin
   * - logo
     - Boolean: true/false
     - true 
     - BIMData's Logo diplayed
   * - rightClickMenu
     - Boolean: true/false
     - true 
     - More options in the right-click
   * - alerts
     - Boolean: true/false
     - true 
     - Alert messages, on the bottom
   * - viewer3DNavCube
     - Boolean: true/false
     - true 
     - XeoKit 3D cube to navigate 

Example with all functionalities disabled
===========================================


.. substitution-code-block:: html
   :linenos:

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
                  bcf: false,
                  reload: false,
                  model: false,
                  help: false,
                  fullscreen: false,
                  section: false,
                  projection: false,
                  selectOptions: false,
                  structureAndProperties: false,
                  bcf: false,
                  logo: false,
                  rightClickMenu: false,
                  viewer3DNavCube: false,
              }
              const accessToken = 'DEMO_TOKEN';
              const { viewer, store, eventHub, setAccessToken } = initBIMDataViewer('app', accessToken, cfg);
          </script>
      </body>

      </html>