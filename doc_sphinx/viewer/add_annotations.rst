===========
Annotations
===========

Adding annotations
===================

To add annotations on objects, simply emit the ``create-annotations``
event to the Event Hub. 

You must provide:
* object IDs
* a priority (``low``,``medium`` or ``high``)
* an index that is displayed on the annotation

.. code-block:: javascript

   this.$hub.emit("create-annotations", {
     ids: [/* object ids */],
     index: 0,
     priority: "low" // "low", "medium" or "high"
   });


Deleting annotations
======================

To delete all annotations, emit ``clear-annotations`` event to the Event
Hub.

.. code-block:: javascript

    this.$hub.emit("clear-annotations");


Code Example
===============

* Opening the plugin activates the **annotation mode**.
* When clicking an object, an annotation is added on it.
* You must select a priority value on the list to display the annotation. If you try to add an annotation without it, an alert warns you that no priority is selected
* Closing the plugin delete all annotations.

.. code-block:: html

   <!DOCTYPE html>
   <html lang="en" dir="ltr">

   <head>
     <meta charset="utf-8">
     <title>BIMData - Annotations</title>
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
           default: false,
           alerts: true,
         }
       }
       const accessToken = 'DEMO_TOKEN';
       const { viewer } = initBIMDataViewer('app', accessToken, cfg);

       viewer.registerPlugins([{
         name: "annotations",
         component: {
           template: `
           <div>
             <select v-model="priority" style="width: 100%;">
               <option disabled value="">Priority</option>
               <option value="low">Low</option>
               <option value="medium">Medium</option>
               <option value="high">High</option>
             </select>
             <input type="number" v-model="index" style="text-align: center;">
           </div>
           `,
           data() {
             return {
               priority: "",
               pickSubscription: null,
               index: 1
             };
           },
           props: ["active"],
           watch: {
             active: {
               handler(active) {
                 const viewer3D = this.$plugins.viewer3D;
                 viewer3D.selectOnClick = !active;
                 // viewer3D.highlightOnHover = !active; // To remove the highlight on hover
                 if (active) {
                   document.body.style.setProperty("cursor", "copy", "important");
                   this.pickSubscription = viewer3D.xeokit.cameraControl.on(
                     "picked",
                     pickResult => {
                       if (!this.priority) {
                         return this.$hub.emit('alert', { type: 'warning', message: 'You must select a priority.' });
                       }
                       if (!pickResult || !pickResult.entity) return;
                       this.$hub.emit("create-annotations", {
                         ids: [pickResult.entity.id],
                         index: this.index,
                         priority: this.priority
                       });
                     }
                   );
                 } else {
                   document.body.style.removeProperty("cursor");
                   viewer3D.xeokit.cameraControl.off(this.pickSubscription);
                   this.index = 1;
                   this.priority = "";
                   this.$hub.emit("clear-annotations");
                 }
               }
             }
           }
         },
         display: {
           iconPosition: "left"
         },
         keepActive: true
       }])
     </script>
   </body>

   </html>

.. raw:: html
   :file: ../_static/viewer_add_annotations_example.html
