.. meta::
   :github: https://github.com/bimdata/documentation/blob/dev/doc_sphinx/viewer/parameters.rst

=========================
Parameters and methods
=========================

You can change the display of the Viewer using the value of attributes, and using the methods.

Attributes
============

List of attributes of the ````BIMDataViewer````.

*	``.helper``: instance of *ViewerHelper* (Type: *object*)
*	``.iframe``: the *HTMLElement* <iframe>
*	``.elementHovered``: name of the element (Type: *string*), read-only
*	``.elementsHovered``: list of names of the elements, read-only
*	``.elementHighlighted``: name of the element (Type: *string*)
*	``.elementSelected``: name of the element (Type: *string*)
*	``.elementsHighlighted``: list of names of the elements (Type: *array*)
*	``.elementsSelected``: list of names of the elements (Type: *array*)
*	``.elementsHided``: list of names of the elements (Type: *array*)
*	``.elementsGhosted``: list of names of the elements (Type: *array*)
*   ``.buttonsMenuActivated``: { [ buttonId ]: *boolean* isActivated?  } (Type: *Object*), read-only 
*   ``.buttonsMenuShowed``: { [ buttonId ]: *boolean* isVisible } (Type: *Object*), read-only

Methods
==========

The interface BIMDataViewerInterface let you have actions on the Viewer via many methods.

Delete
--------

*	``BIMDataViewer.drop( )``: deletes the BIMViewer - returns *void*

Window
-------

All these methods return *void*, except ``onCustomWindow`` (see above).

.. js:method:: BIMDataViewer.addCustomWindow(id, options)

   :param string id: ID of the Window
   :param object options: Instance of BIMViewerParamsCustomWindowOptions
   :returns: void

*	``BIMDataViewer.addCustomWindow()``: creation of a custom window, initialization with the parameters given in the ``options`` Object
        
        **Parameters:**
            * *string* id: ID of the Window  
            * ``options``: *Object* ``BIMViewerParamsCustomWindowOptions`` 
        **Usage**
            ```.. code-block:: javascript

                    viewer1.addCustomWindow('first-window', {
                        open: true,
                        template: 'awesome'
                    })
            
*   ``BIMDataViewer.addCustomButtonMenu()``:
        
        **Parameters:**
            * id: *string* ID of the Menu,
            * options: *Object* BIMViewerCustomButtonOptionsMenu
*	``BIMDataViewer.removeCustomWindow()``:
        
        **Parameters:**
            * id: *string* ID of the custom Window
*	``BIMDataViewer.openCustomWindow()``:
        
        **Parameters:**
            * id: *string* ID of the custom Window
*	``BIMDataViewer.closeCustomWindow()``:
        
        **Parameters:**
            * id: *string* ID of the custom Window
*	``BIMDataViewer.setCustomWindowTemplate()``:
        
        **Parameters:**
            * id: *string* ID of the custom Window
            * template: *string* name of the template
*	``BIMDataViewer.onCustomWindow()``:
        
        **Parameters:**
            * idWindow: *integer* ID of the custom Window
            * event: *string* name of the event 
            * selector: *string* CSS-style selector
            * callback: *Function* [callback]
            * preventDefault: *boolean*
        
        **Returns:**
            * windowNumber: *integer* auto-increment numeration of the custom Windows
*	``BIMDataViewer.offCustomWindow()``:
        
        **Parameters:**
            * id: *string* ID of the custom Window

Buttons
----------

Methods to interact with buttons.
All these methods return *void*.

*	``BIMDataViewer.activateButtonMenu()``:
        
        **Parameters:**
            * target: 
            * visibility: *boolean*
*	``BIMDataViewer.showButtonMenu()``:
        
        **Parameters:**
            * target: 
            * visibility: *boolean* 
*	``BIMDataViewer.showSelectModeMenu``:
        
        **Parameters:**
            * target: 
            * visibility: *boolean*
*	``BIMDataViewer.addCustomButtonMenu``:
        
        **Parameters:**
            * id: *integer* ID of the menu
            * options: *Object* instance of ``BIMViewerCustomButtonOptionsMenu``
*	``BIMDataViewer.removeCustomButtonMenu()`` :
        
        **Parameters:**
            * id: *integer* ID of the menu


Reach the Viewer
-----------------

More generic methods to reach the Viewer and set it:

*	``BIMDataViewer.on()``:
        **Parameters:**
            * eventName: *string* name of the targeted event
            * callback: *Function* [callback]
        **Returns:**
            * number: an auto-increment ID for this Viewer instance
*	``BIMDataViewer.off()``:
        **Parameters:**
            * id: *integer* ID of the Viewer
        **Returns:**
            * *void*


Elements & IFC
----------------

Methods to interact with elements of your model:

*	``BIMDataViewer.setPickable()``: set an element of the model as pickable for selection
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * *void*
*	``BIMDataViewer.setUnpickable()``: set an element of the model as non-pickable for selection
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * *void*
*	``BIMDataViewer.getElementsInfo()``: get an element/collection of elements of your model and their informations
        **Parameters:**
            * icdId: *integer* 
        **Returns:**
            * Element(s) *Object(s)*: { [id: string]: any }
*	``BIMDataViewer.getModel()``: get the Model object
        **Parameters:**
            * uuid: *integer* 
        **Returns:**
            * *string*
*	``BIMDataViewer.getStructure()``:
        **Parameters:**
            * uuid: *integer* 
        **Returns:**
            * Promise *Function*


Interface
---------
Methods to modify display, view and point of view:

*	``BIMDataViewer.getColor()``:
        **Parameters:**
            * id: *integer* ID of the IFCElement
        **Returns:**
            * color: Promise<[ *number*, *number*, *number* ]
*	``BIMDataViewer.setColor()``:
        **Parameters:**
            * selector: *string* 
            * color: *array* [ *number*, *number*, *number* ]
        **Returns:**
            * returns *void*
*	``BIMDataViewer.getSnapshot()``:
        **Parameters:**
            * options: *Object* { *integer* width, *integer* height, *string* format: "png|jpg" }
        **Returns:**
            * color: *string*
*	``BIMDataViewer.getViewpoint()``:
        **Returns:**
            * returns *Object* instance of <ViewPoint>
*	``BIMDataViewer.setViewPoint()``:
        **Parameters:**
            * viewpoint: *Object* instance of <ViewPoint>
        **Returns:**
            * returns *void*
*	``BIMDataViewer.viewFit()``: focus on the given element(s)
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
*	``BIMDataViewer.select()``:
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
*	``BIMDataViewer.deselect()``:
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
*	``BIMDataViewer.highlight()``: put the element(s) in the highlight color
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
*	``BIMDataViewer.dehighlight()``: remove the highlight from the element(s)
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
*	``BIMDataViewer.show()``:
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
*	``BIMDataViewer.hide()``:
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
*	``BIMDataViewer.unghost()``: no more transparency for the given element(s)
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
*	``BIMDataViewer.ghost()``: set transparency to the maximum for the given element(s)
        **Parameters:**
            * selector: *string* CSS-style selector
        **Returns:**
            * returns *void*
