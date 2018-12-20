================================
Create a new Viewer
================================

You will need to have your accessToken, and the info about the IFC file you want to init the Viewer with: the cloud ID, the project ID, and the IFC ID.
These pieces of information are useful to set a new Viewer object in your JS program.


Constructor
------------

The instanciation of the `BIMDataViewer` requires:

 * {String}: ID of DOM container element to append the viewer's canvas to, probably a `<div>` element
 * {Object}: Configuration for the Viewer with this attributes as strings:
    * accessToken
    * cloudId
    * projectId
    * ifcId
 * {Boolean} (default = *false*) Whether to make the viewer canvas transparent, which would allow the container to show through.
 * {String} (default = *'fr'*) Selects the current localisation language 


The code snippet
-----------------

.. code-block:: javascript

    var myAccessToken = 'DEMO_TOKEN';
    var myCloudId = 88;
    var myProjectId = 100;
    var myIfcId = 175;
    
    var viewer = new BIMDataViewer('my-div', {
    accessToken: myAccessToken,
    cloudId: myCloudId,
    projectId: myProjectId,
    ifcId: myIfcId
    });

