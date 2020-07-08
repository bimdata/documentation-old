=======================
Managing Section Planes
=======================


Creating Section Planes
=======================

To add a section, you must first enter in **Section mode**.

.. code-block:: javascript

    this.$hub.emit("set-section-mode", { active: true });

.. note::
    
    Remember to quit Section mode when you are done, by setting **active** to *false*.

Now you can create Section planes!


By axis
--------

You can specify the axis and the section is made on this axis, at the center of the scene bounding box.

.. code-block:: javascript

   this.$hub.emit(
     "create-section-plane",
     {
       axis: "x" // "x", "y" or "z"
     }
   );



By position and direction
-----------------------------

You can specify a position and a direction. 
Position and direction both are Arrays of length 3.

.. code-block:: javascript

   this.$hub.emit(
     "create-section-plane",
     {
       position: new Float32Array(3),
       direction: new Float32Array(3)
     }
   );



Deleting Section Planes 
=========================

To delete the displayed section plane:

.. code-block:: javascript

   this.$hub.emit("delete-section-plane");


To **delete all** section planes:

.. code-block:: javascript

   this.$hub.emit("delete-all-section-planes");


Example
============

* Clicking the plugin icon will activate the ``cutting`` mode. 
* You can now click an object and a section plane is added to its surface. You can add multiple section planes. 
* To delete section planes, close the plugin.

.. code-block:: html

   <!DOCTYPE html>
   <html lang="en" dir="ltr">

   <head>
     <meta charset="utf-8" />
     <title>BIMData - Section on surface</title>
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
           default: false
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
           name: "SectionOnSurfacePlugin",
           component: {
             render() {
               return null;
             },
             data() {
               return {
                 pickSurfaceSubscription: null
               };
             },
             props: ["active"],
             watch: {
               active: {
                 handler(active) {
                   const viewer3D = this.$plugins.viewer3D;
                   this.$hub.emit("set-section-mode", { active });
                   viewer3D.selectOnClick = !active;
                   // viewer3D.highlightOnHover = !active; // To remove the highlight on hover
                   if (active) {
                     document.body.style.setProperty(
                       "cursor",
                       "crosshair",
                       "important"
                     );
                     this.pickSurfaceSubscription = viewer3D.xeokit.cameraControl.on(
                       "pickedSurface",
                       pickResult => {
                         if (!pickResult) return;
                         this.$hub.emit(
                           "create-section-plane",
                           {
                             position: new Float32Array(pickResult.worldPos),
                             direction: new Float32Array(pickResult.worldNormal)
                           }
                         );
                       }
                     );
                   } else {
                     document.body.style.removeProperty("cursor");
                     viewer3D.xeokit.cameraControl.off(
                       this.pickSurfaceSubscription
                     );
                     this.$hub.emit(
                       "delete-all-section-planes"
                     );
                     // this.$hub.emit("delete-section-plane"); // To delete the active section plane
                   }
                 }
               }
             }
           },
           display: {
             iconPosition: "left"
           },
           keepActive: true
         }
       ]);
     </script>
   </body>

   </html>

.. raw:: html
   :file: ../_static/viewer_examples/viewer_section_planes_example.html
