:active_page: viewer

================
Async plugins
================

Description
==============

If your plugin is on the right or left Viewer Menu, you can declare it as ``async``:

.. code-block:: javascript

    // plugin code
    {
      ...
      asyncLoading: true,
      ...
    }


Once your plugin is declared as ``async``, clicking on the menu button (left or right) triggers the plugin loading.
Until the correct event is emited, clicking on the menu button again will have no effect. The same behaviour occured when you deactivate your plugin (click on the menu button while plugin is displayed and loading is finished). While loading/unloading, the plugin icon will be changed by a spinner indicating that an action is in progress.

The reason to use async plugins is preventing icon click-spam errors.

For example: while unloading a plugin, data are unloaded too and we want to be sure that these data are correctly unloaded until the plugin opens again.

The events to stop loading are:

* ``loading-end`` while the plugin stop loading
* ``unloading-end`` while the plugin finish unloading

Example : A simple async plugin
================================

A simple async plugin that takes time to load/unload. 
While loading/unloading, clicking on the plugin button has no effect.

.. raw:: html
   :file: ../_static/viewer_async_plugin_example.html

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en" dir="ltr">

    <head>
      <meta charset="utf-8" />
      <title>BIMData - Async Plugin</title>
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
            name: "asyncPlugin",
            component: {
              render() {
                return null;
              },
              props: ["active"],
              watch: {
                active(active) {
                  const eventName = active ? "loading-end" : "unloading-end";
                  setTimeout(() => this.$emit(eventName), 2000);
                }
              }
            },
            display: {
              iconPosition: 'left'
            },
            asyncLoading: true // THE ASYNC PLUGIN CONFIG
          }
        ]);
      </script>
    </body>

    </html>