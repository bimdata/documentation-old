===========================================
How-to embed the Viewer using Vue.js
===========================================

.. contents:: Table of Contents
   :depth: 2

Pre-Requisites
===============

* a Vue JS application
* `Vue.js framework`_  >= 2.6
* `VueX`_
* `Vue I18n`_
* `BIMData Viewer`_: install the npm package

.. _Vue.js framework: https://vuejs.org
.. _VueX: https://vuex.vuejs.org/
.. _Vue I18n: https://kazupon.github.io/vue-i18n/
.. _BIMData Viewer: https://www.npmjs.com/package/@bimdata/viewer


Work with the newest Viewer version
=====================================

To get the latest Viewer version, the npm install process delivers you the proper version.

.. code-block:: bash

    npm i @bimdata/viewer

The Viewer in your web page
============================

The BIMData Viewer is built with Vue.js. In this examples, we assume that you know about Vue.js and you had the dependencies installed.

.. code-block:: bash

  npm install vuex
  npm install vue-i18n

The `app.vue` file
====================

In your `app.vue` file

 * load the Viewer package
 * set the data about which IFC model you load
 * then add the options you want

The script part
----------------

.. code-block:: javascript
   :linenos:

    import BIMDataViewer from '@bimdata/viewer'

    export default {
        name: 'app',
        data() {
          return {
            cfg: {
              cloudId: 88,
              projectId: 100,
              ifcIds: [175],
              apiUrl: "https://api-beta.bimdata.io",
            }
          }
        },
        components: {
          BIMDataViewer
        }
    }

Template
------------

In the template part, you need to set the height of its container.

In the `app.vue` file:

.. code-block:: html
   :linenos:

    <template>
        <div id="app">
            <BIMDataViewer accessToken="DEMO_TOKEN" :cfg='cfg' style="height:100vh;"/>
        </div>
    </template>


The `main.js` file
===================

In the `main.js` file:


 * import all dependencies: vue, i18n, vuex
 * set i18n object: specify the locale and fallback
 * set store object: using i18n, to store all data about your model

.. note::

    The Viewer is available in french and english languages.

.. code-block:: javascript
   :linenos:
   :caption: File ``main.js``

    import Vue from 'vue'
    import App from './App.vue'
    import VueI18n from 'vue-i18n';
    import Vuex from 'vuex';

    Vue.config.productionTip = false

    Vue.use(VueI18n);
    Vue.use(Vuex);

    const i18n = new VueI18n({
      locale: 'fr',
      fallbackLocale: 'en', // set fallback locale
      messages: {
        en: null,
        fr: null
      }
    })

    new Vue({
      store: new Vuex.Store(),
      i18n,
      render: function (h) { return h(App) }
    }).$mount('#app')


Complete example
=================

All the Viewer's plug-ins are disabled.

.. code-block::
   :linenos:
   :caption: File `app.vue`

    <template>
        <div id="app">
            <BIMDataViewer accessToken="DEMO_TOKEN" :cfg="cfg" style="height:100vh;" />
        </div>
    </template>

    <script>
        import BIMDataViewer from "@bimdata/viewer";

        export default {
        name: "app",
        data() {
          return {
            cfg: {
              cloudId: 88,
              projectId: 100,
              ifcIds: [175],
              apiUrl: "https://api-beta.bimdata.io",
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
              viewer3DNavCube: false
            }
          };
        },
        components: {
          BIMDataViewer
        }
        };
    </script>
