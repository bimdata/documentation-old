================
Modal manager
================

Usage
======


You can access the global modal manager using the ``$plugins`` helper :

.. code-block:: javascript

    this.$plugins.modalManager


The modal manager let you push a modal to display on the Viewer:

.. code-block:: javascript

    this.$plugins.modalManager.pushModal(MyModal);

.. note::
    
    In the example above, ``MyModal`` should be a Vue.js component.

On modals
=========

You can push as many modals as you want.
They will be displayed in the order they have been pushed, as soon as the current modal is closed.


Close a modal
---------------

You can close the current modal from itself or the global context.

From anywhere
^^^^^^^^^^^^^^^

You can close the current modal from anywhere using ``.clearModal()``:

.. code-block:: javascript

    this.$plugins.modalManager.clearModal();


From itself
^^^^^^^^^^^^^^^

You can also from the current modal itself by emitting the ``close`` Event:

.. code-block:: javascript

    // inside modal code
    this.$emit("close");


Example
========

The added plugin will push two modals.
Clicking on the displayed button will close the current modal.

.. raw:: html
   :file: ../_static/viewer_modal_manager_example.html

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en" dir="ltr">

    <head>
    <meta charset="utf-8" />
    <title>BIMData - Modal Manager</title>
    <script src="https://unpkg.com/@bimdata/viewer@0.8.2/dist/bimdata-viewer.min.js" charset="utf-8"></script>
    </head>

    <body>
    <div style="height: 100vh">
        <div id="app"></div>
    </div>
    <script>
        const cfg = {
        cloudId: 88,
        projectId: 100,
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
            name: "modals",
            component: {
            render() {
                return null;
            },
            created() {
                this.$plugins.modalManager.pushModal({
                template: `
                    <div style="margin:10px;">
                    <h1>I am the first modal</h1>
                    <button @click="$emit('close')">Close the first modal</button>
                    </div>`
                });
                this.$plugins.modalManager.pushModal({
                template: `
                <div style="margin:10px;">
                    <h1>I am the second modal</h1>
                    <button @click="$plugins.modalManager.clearModal()">Close the second modal</button>
                    </div>`
                });
            }
            }
        }
        ]);
    </script>
    </body>

    </html>
