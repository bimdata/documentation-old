======================
Programming shortcuts
======================

Here are some useful feature using the `$` (dollar sign) syntax.


The Events Hub
===============

.. code-block:: javascript

   this.$hub;

.. seealso::
    
    Learn about :doc:`all events <events>` you can listen to.


Plugins
========

An object containing all registered plugins.

.. code-block:: javascript

   this.$plugins.pluginIWantToAccess;


Access Token
===============

The Access Token for BIMDataConnect.

.. code-block:: javascript

   this.$utils.getAccessToken();


API Client
============

The client to access BIMData API. 

See https://github.com/bimdata/javascript-api-client for more info about the JavaScript API Client.

.. code-block:: javascript

   this.$bimdataApiClient;


Keyboard shortcuts
======================

The keyboard shortcut manager, useful to register shortcuts.

.. code-block:: javascript

   this.$plugins.keyboardShortcutsManager;

.. seealso::
    
    Read also about :doc:`how-to customize keyboards shortcuts <customize_keyboard_shortcuts>`


Modal manager
================

The modal manager to display global modals.

.. code-block:: javascript
   
   this.$plugins.modalManager;

.. seealso::
    
    Read more :doc:`about async plugins <async_plugins>`.


Selection
=============

A Set of all selected object ids. The same property is present on the getters but returns an Array instead.

.. code-block:: javascript

   this.$utils.getSelectedObjectIds();