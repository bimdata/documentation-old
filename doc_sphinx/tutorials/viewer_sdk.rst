==================
SDK Viewer
==================

The SDK is a development tool helping you to create faster a Viewer plugin. 

It is a Github repository, containing a pre-configured environment to develop BIMData Viewer plugins.
You can develop, test, build, package and share your plugin easily.

.. contents::

Setup
==========

First, you must create a BIMData Application (see :doc:` the Tutorial </tutorials/dev_create_an_application>`).

The SDK needs at least ``cloud:read`` and ``ifc:read`` scopes.

.. note::
    
    The default BCF Plugin needs ``bcf:read`` and ``bcf:write`` scopes. 
    In addition to that, you can add any scope you need for your plugin.

By default, the redirect URI is:  ``http://localhost:8080/oidc-callback``

Then you can copy the ``.env.example`` file and add in it your ``client_id``:

.. substitution-code-block:: bash
    
    npm install
    cp .env.example .env


Edit ``.env`` file with your data (your ``client_id``).

Compiles and hot-reloads for development
------------------------------------------

.. substitution-code-block:: bash

    npm run serve


Usage
========

When going on ``http://localhost:8080``, a simple interface parse your Projects and Models and let you open the one you want.

You can directly open a Project or a Model by opening an URL using specific IDs: http://localhost:8080/viewer?cloudId=391&projectId=634&ifcId=1491

Create your first plugin
-----------------------------

.. substitution-code-block:: bash

    npm run init-plugin


This tool asks you a couple of questions about the plugin you develop to generate from your answers files for your plugin.

Files are created in the directory ``src/plugins/{{name of your plugin}}``.

Then import your newly created plugin ``src/viewer/viewer.vue`` and add it to the ``registerPlugin`` array.

.. substitution-code-block:: javascript

    import SnowflakesPlugin from "@/plugins/snowflakes/src/snowflakes.plugin.js";
    import SplitPlugin from "@/plugins/split/src/split.plugin.js";

    ...
    mounted() {
    this.$refs.bimdataViewerInstance.registerPlugins([
        SnowflakesPlugin,
        SplitPlugin,
    ]);
    }
    ...


 Package your plugin
==============================

To load your plugin in a real environment, you want to package and publish your plugin.

The plugin template is pre-configured with a rollup config that let you do this easily:

.. substitution-code-block :: bash

    cd src/plugins/{your_plugin}
    npm install
    npm run build


This creates a ``dist/`` folder in your plugin directory with a simple JS file. 
This minified file includes the CSS and the assets (encoded in base64). 

.. note::
   
    It's not the most performant way, but it's the simplest and the Viewer loads many mega-bytes models anyway.

You can either copy-paste this file in your environment and load it at your convenience, or you can publish it on NPM.
To publish it, update the ``package.json`` file with the proper information. Then run the **npm publish** command.

.. tip::
    
    The code is minified to protect your code as much as possible.


More info about how it works
=============================

The SDK itself uses **Webpack** to build. The packaging uses **Rollup**. 
If you need a complex JS flow, it may lead to some issues.


To see these issues before deploying, load the packaged version in the SDK:

.. substitution-code-block :: bash

    cd src/plugins/{your_plugin}
    npm run watch

And load the *dist* version of the plugin:

.. substitution-code-block :: javascript

    import SplitPlugin from "@/plugins/split/dist/split.plugin.js";

    ...
    mounted() {
    this.$refs.bimdataViewerInstance.registerPlugins([
        SplitPlugin,
    ]);
    }
    ...


You can also edit the Webpack and Rollup config as you want.
