=========================
Parameters and methods
=========================

You can change the display of the Viewer using parameters, and using the methods.


Parameters
============

List of attributes and parameters for the methods.

*	helper: ViewerHelper;
*	iframe: HTMLElement;
*	readonly elementHovered : string;
*	readonly elementsHovered: string[];
*	elementHighlighted : string;
*	elementSelected    : string;
*	elementsHighlighted: string[];
*	elementsSelected   : string[];
*	elementsHided      : string[];
*	elementsGhosted    : string[];
*	readonly buttonsMenuActivated: { [id: string]: boolean };
*	readonly buttonsMenuShowed: { [id: string]: boolean };


Methods
==========

The interface BIMDataViewerInterface let you have actions on the Viewer via many methods.

Delete
--------

*	drop(): void;

Window
-------

*	addCustomWindow(id: string, options?: BIMViewerParamsCustomWindowOptions): void;
*	removeCustomWindow(id: string): void;
*	openCustomWindow(id: string): void;
*	closeCustomWindow(id: string): void;
*	setCustomWindowTemplate(id: string, template: string): void;
*	onCustomWindow(idWindow: string, event: string, selector: string, callback: Function, preventDefault?: boolean): number;
*	offCustomWindow(id: number): void;

Button
----------

Methods to interact with buttons:

*	activateButtonMenu(target: string, value?: boolean): void;
*	showButtonMenu(target: string, value?: boolean): void;
*	showSelectModeMenu(target: string, value?: boolean): void;
*	addCustomButtonMenu(id: string, options?: BIMViewerCustomButtonOptionsMenu): void;
*	removeCustomButtonMenu(id: string): void;


Reach the Viewer
-----------------

More generic methods to reach the Viewer and set it:

*	on(event: string, callback: Function): number;
*	off(id: number): void;


Elements & IFC
----------------

Methods to interact with elements of your model:

*	setPickable(selector: any):void;
*	setUnpickable(selector: any):void;
*	getElementsInfo(ifcId?: number): { [id: string]: any };
*	getModel(uuid: string): string;
*	getStructure(uuid: string): Promise<any>;


Colors
---------

Methods to modify colors:

*	getColor(id: string): Promise<[ number, number, number ]>;
*	setColor(selector: any, color: [ number, number, number ]): void;


Display and viewing
----------------------

Methods to modify display, view and point of view:

*	getSnapshot(): Promise<any>;
*	getSnapshot(options?: { width?: number, height?: number, format?: "png|jpg" }): Promise<string>;
*	getViewpoint(): Promise<ViewPoint>;
*	setViewPoint(viewPoint?: ViewPoint): void;
*	viewFit(selector?: string|string[]): void;
*	select(selector?: any): void;
*	deselect(selector?: any): void;
*	highlight(selector?: any): void;
*	dehighlight(selector?: any): void;
*	show(selector?: any): void;
*	hide(selector?: any): void;
*	unghost(selector?: any): void;
*	ghost(selector?: any): void;

