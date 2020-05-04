=====================
Customize the Viewer
=====================

.. 
    excerpt
        Make the Viewer best suited to your needs.
    endexcerpt


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

The Viewer is provided with many functionalities by default. Each one can be disabled independently.
In the ``cfg`` Object (see ::doc:`/getting_started/viewer` ), you can disable any plugin by setting it to ``false``:

Each functionality has a default value and could be disabled.

.. list-table:: Viewer functionalities
   :header-rows: 1
   :widths: 10 40 40

   * - Name
     - Description
     - When set to false...
   * - reload
     - Button in the UI. Click on it reload the checked models.
     - Remove the button.
   * - model
     - Display a list of the Project's Models.
     - The list is not displayed.
   * - help
     - Help icon, linked to the [?] keyboard shortcut. When the icon or the key is hit, the help modal is displayed.
     - The help icon and the shortcut are not provided.
   * - section
     - Section tool plugin: the Model is sectionable on 3 plans (x, Y and Z).
     - The plugin is disabled.
   * - projection
     - Projection selection plugin: perspective, first person or orthogonal.
     - The plugin is disabled and the projection is perspective.
   * - selectOptions
     - Choice of the selection mode: section by object or selection by type.
     - The plugin is disabled, the selection is by object.
   * - structureAndProperties
     - List structure and properties, in window manager based panels.
     - Disabled the structure and properties plugin.
   * - bcf
     - BCF plugin is available.
     - The BCF plugin is disabled
   * - logo
     - BIMData's Logo diplayed
     - No logo is diplayed.
   * - rightClickMenu
     - The right-click shows a custom menu, keyboard shortcuts are attached to these functionalities.
     - The default browser's menu only is available.
   * - alerts
     - The Alert plugin captures and displays the messages, at the bottom of the Viewer.
     - The plugin is disabled. Messages are not diplayed.
   * - viewer3DNavCube
     - XeoKit 3D cube to navigate
     - The navigation 3D cube is not diplayed.

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
              bimdataPlugins: {
                bcf: false,
                reload: false,
                model: false,
                help: false,
                fullscreen: false,
                section: false,
                projection: false,
                selectOptions: false,
                structureAndProperties: false,
                logo: false,
                rightClickMenu: false,
                viewer3DNavCube: false,
              }
            }
            const accessToken = 'DEMO_TOKEN';
            const { viewer, store, eventHub, setAccessToken } = initBIMDataViewer('app', accessToken, cfg);
          </script>
      </body>

      </html>
