=================================
Adding Context Commands
=================================


You can add context commands to the Right-click Menu.
Context commands are specific to the location the user right-clicked.

Right-Click Menu Command
=========================

To add command to the right-click menu, get the right-click menu plugin and register a command
in created or mounted `component lifecyle
method <https://vuejs.org/v2/guide/instance.html#Instance-Lifecycle-Hooks>`__.

.. warning::

    The ``rightClickMenu`` is *Undefined* if you deactivate it on the Viewer ``cfg``.

.. code-block:: javascript

    const rightClickMenu = this.$plugins.rightClickMenu;

    rightClickMenu.registerCommand({
      label: "My custom command",     // The text displayed on the Right-click menu
      picto: "K",                     // A character displayed after the text
      execute: () => null,            // A function that executed when the command is clicked
      predicate: () => null           // A function executed when the Right-click menu opens
    });

Parameters
-----------

================  ===================  =============================================================================================
parameter         type                  Description
================  ===================  =============================================================================================
label             String               The text displayed on the Right-click menu
picto             character            A character displayed after the text (usually to show the corresponding  keyboard shortcut)
execute           Function()           A function executed when the command is clicked on the Right-click menu
predicate         Function()           A function executed when the right click menu opens.
                                       The command is displayed if the function returns **true**.
================  ===================  =============================================================================================


Adding Context Commands
=========================

To add context commands, your Component should react on user right-click:

.. code-block:: html

   <!-- in your component template -->
   ...
   <div @click.right="onRightClick()">
     Right-click zone
   </div>
   ...

Then, you need to get the Right-click Menu plugin and register the context command.


.. note::

    The ``rightClickMenu`` is *Undefined* if you deactivate it on the Viewer ``cfg``.


.. code-block:: javascript

   const MyComponent = {
     ...
     methods: {
       onRightClick() {
         // get the right-click menu plugin
         const rightClickMenu = this.$plugins.rightClickMenu;
         // register context command
         rightClickMenu.registerContextCommand({
           label: "My context command",
           execute: () => {
             console.log('Context command executed');
           }
         });
       }
     }
   }

The command is an object with two properties :

* label: the text displayed on the Right-click menu
* execute: a function executed when the user click on the newly added right-click menu command

Example
=========

* Open the plugin and right-click on the ‘Data’ area.
* Edit command is added to the right-click context menu.
* Click on Edit to turn the ‘Data’ area into edit mode where you can change the text.
* Press enter to validate the new text.

.. code-block:: html

   <!DOCTYPE html>
   <html lang="en" dir="ltr">
     <head>
       <meta charset="utf-8" />
       <title>BIMData - Context Menu</title>
       <script
         src="https://unpkg.com/@bimdata/viewer@^0.8.22/dist/bimdata-viewer.min.js"
         charset="utf-8"
       ></script>
     </head>

     <body>
       <div style="height: 100vh">
         <div id="app"></div>
       </div>
       <script>
         const cfg = {
           cloudId: 88,
           projectId: 100,
           ifcIds: [],
           bimdataPlugins: {
             default: false,
             rightClickMenu: true, // Right click menu should be activated
           }

         };
         const accessToken = "DEMO_TOKEN";
         const { viewer, store, eventHub, setAccessToken } = initBIMDataViewer(
           "app",
           accessToken,
           cfg
         );
         viewer.registerPlugins([
           {
             name: "myCustomPlugin",
             component: {
               template: `
          <div class="context">
            <div @click.right="onRightClick()">
              <input
                ref="input"
                v-if="editMode"
                v-model="data"
                @keyup.enter="validate()"
              />
              <span v-else>{{ data || 'no data provided' }}</span>
            </div>
          </div>
          `,
               data() {
                 return {
                   editMode: false,
                   data: "Data"
                 };
               },
               methods: {
                 validate(number) {
                   this.editMode = false;
                 },
                 onRightClick(number) {
                   const rightClickMenu = this.$plugins.rightClickMenu;
                   if (rightClickMenu) {
                     rightClickMenu.registerContextCommand({
                       label: "Edit",
                       execute: () => {
                         this.editMode = true;
                       }
                     });
                   }
                 }
               }
             },
             keepActive: true,
             display: {
               iconPosition: 'left',
               content: 'simple'
             },
             tooltip: "myCustomPlugin"
           }
         ]);
       </script>
     </body>
   </html>

.. raw:: html
   :file: ../_static/viewer_examples/viewer_custom_context_commands_example.html
