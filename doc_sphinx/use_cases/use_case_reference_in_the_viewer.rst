=======================================
Use-case: the reference in the Viewer
=======================================

..
    excerpt
        Discover a usage of the Viewer to display reference manuals
    endexcerpt


Purpose
========

Use the Viewer to display the reference of the documentation for a set of equipment gears.

The result
=============

For an ensemble of elements, we want to attach a link of the documentation, directly in the Viewer.
We have a list of the elements' UUIDs, and using the BIMData API, we send request to get the properties of each element.


Then, using the properties in the Pset_ManufacturerTypeInformation pset (ie: element's name, year, model, Manufacturer, etc.), 
we search in an external database the reference of the user's manual.


Finally, we add an annotation to the element in the Viewer: this annotation contains the link to the the User's Manual of the element.