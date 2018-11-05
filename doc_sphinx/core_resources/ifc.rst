.. index::
   single: execution; ifc
   module: core

====
IFC
====



BimData API exposes a lot of tools for extract, update and manipulate information from IFC files.
Upload an IFC

To upload an IFC, you have to upload a document. If the API detects an IFC (based on the file name ending with .ifc or .ifczip), it will trigger the IFC process.

IFCs are tied to a document which represents the actual uploaded file.
Workflow

After being uploaded, the IFC will be processed on our servers.
Note

The process takes from few minutes to an hour depending on the size of the file and the options enabled.

You can follow the progress on the status field:



================  ===================  =================================================================
status            Name of the status   Description
================  ===================  =================================================================
P                  Pending             Your IFC will soon be processed
I                  In process          The process has started
C                  Completed           The process is complete and you can retrieve data from the API
E                  Error               The process has failed.
================  ===================  =================================================================


It's more likely to be a problem on our side. An alert is triggered and our team will fix it promptly.

Once the process is completed, you can:

* Retrieve and update zones and spaces
* Retrieve and update elements and properties
* Retrieve the model
* Retrieve the structure
