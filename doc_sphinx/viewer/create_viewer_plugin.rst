=================================================
Tutorial: How-to create a plug-in for the Viewer
=================================================

..
    excerpt
        Create your first Viewer plug-in
    endexcerpt

A Viewer's plug-in is a Vue.js Component. The plug-in adds one or more features to the Viewer.
Enrich your Model with external data, trigger events during navigation in the 3D model, and provide to your users an unforgettable experience.

Pre-requisites
=================
* `VueJS framework`_ >= 2.6
* `VueX`_
* `Vue I18n`_
* `BIMData Viewer`_: install the npm package
* Knowledge about Vue.js components: https://vuejs.org/v2/guide/components.html

.. note::
     
    For this tutorial, we recommend the usage of Vue CLI: https://cli.vuejs.org

.. _VueJS framework: https://vuejs.org
.. _VueX: https://vuex.vuejs.org/
.. _Vue I18n: https://kazupon.github.io/vue-i18n/
.. _BIMData Viewer: https://www.npmjs.com/package/@bimdata/viewer

Overview of the steps:
=======================

 #. Prepare your environment
 #. Using Vue CLI, create a Vue.js project
 #. Customize App.vue
 #. Create a Vue.js Component

.. contents:: Table of Contents
   :depth: 2

Prepare your environment
=========================

Install Vue.js.
Then install also i18n, vuex and the Viewer.

That means lauching these commands:

.. code-block:: bash

    npm install i18n
    npm install vuex
    npm install @bimdata/viewer


Create a Vue.js project
========================

.. code-block:: bash

    vue create my-first-plugin
    cd my-first-plugin

With the command ``npm run serve``, you view your Vue.js app with the Viewer in your browser, by default at: http://localhost:8080/ 

In the directory `components/` create a file named `MyComponent.vue`: this file hosts the code of your plug-in.

Customize the App.vue file
============================

Open the default created `App.vue` file in your code editor.
Remove entirely the ``<style>`` element, we do not use it in this tutorial.

.. code-block:: xml
   :caption: App.vue file, template part

    <template>
    <div id="app">
        <BIMDataViewer
        ref="viewer"
        accessToken="DEMO_TOKEN"
        :cfg="cfg"
        style="height:100vh;"
        />
    </div>
    </template>

The :cfg is about the configuration of the Viewer.
The ref allows us to use the viewer as the parent of the plug-in element, using the $refs var.

See the Vue.js documentation about $ref: https://vuejs.org/v2/api/#ref

.. tip:: 
    
    Replace the ``accessToken`` by yours when you have one.


<script> element
------------------

Instead of the Helloworld, import the Viewer, like so:

.. substitution-code-block:: javascript
   :caption: App.vue file, imports

    <script>
        import BIMDataViewer from "@bimdata/viewer";
        import MyComponent from "./components/MyComponent";


Set the template for your BIMDataViewer Vue.js Component.

.. warning::

    Define in your CSS the minimal size of the Viewer container using the style attribute in this tutorial. 
    The Viewer cannot fill its parent element.

In the ``<script>`` element, define the cfg object that defines the settings for the Viewer.
We chose to remove BCF plugin, and the logo for our Viewer.

.. substitution-code-block:: javascript
   :caption: App.vue file
   :lineno-start: 42

        data() {
            return {
            cfg: {
                cloudId: 88,
                projectId: 100,
                ifcIds: [175],
                apiUrl: "https://api-beta.bimdata.io",
                bcf: false,
                logo: false,
            }
            }
        }
    }

Add the mounted() part:

.. substitution-code-block:: javascript
   :caption: App.vue file
   :lineno-start: 18

    mounted() {
        this.$refs.viewer.registerPlugins([
        {
            name: "myCustomPlugin",
            component: MyComponent,
            position: "left-menu",
            display: "menu",
            keepActive: true,
            tooltip: "myCustomPlugin.tooltip",
            i18n: {
            en: {
                myCustomPlugin: {
                tooltip: "English Tooltip",
                }
            },
            fr: {
                myCustomPlugin: {
                tooltip: "French Tooltip",
                }
            }
            }
        }
        ]);
    },



Configure the BIMDataViewer Component.

.. substitution-code-block:: javascript
   :caption: File `App.vue`
   :lineno-start: 65

    components: {
        BIMDataViewer
    }

The complete ``App.vue`` file
------------------------------

Below this is a complete version of the ``App.vue`` file, with all the Viewer options set to ``false``.

.. substitution-code-block::
   :caption: File `App.vue` (complete file)
   :linenos:

    <template>
    <div id="app">
        <BIMDataViewer
        ref="viewer"
        accessToken="DEMO_TOKEN"
        :cfg="cfg"
        style="height:100vh;"
        />
    </div>
    </template>

    <script>
    import BIMDataViewer from "@bimdata/viewer";
    import MyComponent from "./components/MyComponent";

    export default {
    name: "app",
    mounted() {
        this.$refs.viewer.registerPlugins([
        {
            name: "myCustomPlugin",
            component: MyComponent,
            position: "left-menu",
            display: "menu",
            keepActive: true,
            tooltip: "myCustomPlugin.tooltip",
            i18n: {
            en: {
                myCustomPlugin: {
                tooltip: "English Tooltip",
                }
            },
            fr: {
                myCustomPlugin: {
                tooltip: "French Tooltip",
                }
            }
            }
        }
        ]);
    },
    data() {
        return {
        cfg: {
            cloudId: 88,
            projectId: 100,
            ifcIds: [175],
            apiUrl: "https://api-beta.bimdata.io",
            reload: false,
            alerts: false,
            model: false,
            help: false,
            fullscreen: false,
            section: false,
            projection: false,
            selectOptions: false,
            structureAndProperties: false,
            // bcf: false,
            logo: false,
            rightClickMenu: false,
            viewer3DNavCube: false
        }
        };
    },
    components: {
        BIMDataViewer
    }
    };
    </script>




Create a Vue.js Component
=========================

Create a file to put the code of your plug-in.

In the components/ directory, create a file named MyComponent.vue.
This file contains the code of your plug-in.


Layout
=======

Each plug-in is associated with a control in the UI: button or keyboard key or shortcut.
The diplay of your plug-in is available in 3 styles:
* Free
* Menu mode
* Window mode


Free
------

Trigger the rendering of your plug-in to the entire screen on the position top:0;


Menu mode
-----------

Trigger the rendering of your plug-in with an icon to the menus.

Available options:

 * left-menu
 * right-menu
 * center 


Window mode
-------------

Trigger the rendering of your plug-in to a modal panel movable and resizeable.
