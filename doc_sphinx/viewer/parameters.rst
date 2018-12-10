=========================
Parameters and methods
=========================

You can change the display of the Viewer using value of attributes, and using the methods.


Attributes
============

List of attributes and parameters for the methods.

*	helper: *ViewerHelper*
*	iframe: *HTMLElement*
*	readonly elementHovered : *string*
*	readonly elementsHovered: *string[]*
*	elementHighlighted : *string*
*	elementSelected    : *string*
*	elementsHighlighted: *string[]*
*	elementsSelected   : *string[]*
*	elementsHided      : *string[]*
*	elementsGhosted    : *string[]*
*	readonly buttonsMenuActivated: { [ id ]: boolean }
*	readonly buttonsMenuShowed: { [ id ]: boolean }


Methods
==========

The interface BIMDataViewerInterface let you have actions on the Viewer via many methods.

Delete
--------

*	``drop( )`` - returns *void*

Window
-------

*	``addCustomWindow`` ( id, ``options``?: ``BIMViewerParamsCustomWindowOptions``) - returns *void*
*	``removeCustomWindow`` ( id) - returns *void*
*	``openCustomWindow`` ( id) - returns *void*
*	``closeCustomWindow`` (  id ) - returns *void*
*	``setCustomWindowTemplate`` (  id , *template* ) - returns *void*
*	``onCustomWindow`` ( ``idWindow``, event, selector, callback, preventDefault? ) - returns *number*
*	``offCustomWindow`` (  id ) - returns *void*

Button
----------

Methods to interact with buttons:

*	``activateButtonMenu`` ( target, visibility: *boolean* ) - returns *void*
*	``showButtonMenu`` ( target, visibility: *boolean* ) - returns *void*
*	``showSelectModeMenu`` ( target, visibility: *boolean* ) - returns *void*
*	``addCustomButtonMenu`` (  id , options: *BIMViewerCustomButtonOptionsMenu* ) - returns *void*
*	``removeCustomButtonMenu`` (  id ) - returns *void*


Reach the Viewer
-----------------

More generic methods to reach the Viewer and set it:

*	``on`` ( eventName, callback) - returns *number*
*	``off`` (  id ) - returns *void*


Elements & IFC
----------------

Methods to interact with elements of your model:

*	``setPickable`` ( selector )- returns *void*
*	``setUnpickable`` ( selector )- returns *void*
*	``getElementsInfo`` ( ``ifcId`` ) { [ id ] }
*	``getModel`` ( id ) - returns *string*
*	``getStructure`` ( id ) - returns *Promise*


Colors
---------

Methods to modify colors:

*	``getColor`` (  id ) - returns Promise<[ *number*, *number*, *number* ]>
*	``setColor`` ( selector, color: [ *number*, *number*, *number* ]) - returns *void*


Display and viewing
----------------------

Methods to modify display, view and point of view:

*	``getSnapshot`` ( ) 
*	``getSnapshot`` ( options: { width?, height?, format: "png|jpg" }) returns *<string>*
*	``getViewpoint`` ( ) - returns *object <ViewPoint>*
*	``setViewPoint`` ( ViewPoint instance) - returns *void*
*	``viewFit`` ( selector: *string|string[]* ) - returns *void*
*	``select`` ( selector ) - returns *void*
*	``deselect`` ( selector ) - returns *void*
*	``highlight`` ( selector ) - returns *void*
*	``dehighlight`` ( selector ) - returns *void*
*	``show`` ( selector ) - returns *void*
*	``hide`` ( selector ) - returns *void*
*	``unghost`` ( selector ) - returns *void*
*	``ghost`` ( selector ) - returns *void*

