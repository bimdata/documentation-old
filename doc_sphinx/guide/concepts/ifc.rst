===
IFC
===

.. 
    excerpt
        After being uploaded, the IFC is processed on our servers.
    endexcerpt

.. container:: columns

    .. container:: content-left

        BIMData API exposes a lot of tools for extract, update and manipulate information from `IFC files`_.

        The tools are compatible with IFC2x3TC1 and IFC4 Add2.

    .. container:: content-right

        .. figure:: /_images/guide/concepts_ifc.png
            :scale: 70%
            :alt: Schema of a Cloud containing Projects with IFC files in it (in yellow)

Depending on the options you chose, you can:

* Retrieve the model as a 3D GLTF file
* Retrieve elements and properties
* Retrieve the spatial structure
* Retrieve classifications, systems and zones
* Retrieve 2D plans in SVG format

Upload an IFC
=============

To upload an IFC file, you have to upload a ``document``. 
When the BIMData API detects an IFC format (based on the file name ending with ``.ifc`` or ``.ifczip``), it will trigger the IFC process.

IFC files are tied to a ``document`` which represents the actual uploaded file.

We use HTTP Compression to speed up the file transfer. HTTP Compression will start as soon as you upload a file.
Files are decompressed at the output of the API.

There is no size limit to the IFC upload.

.. note::

    The displayed filesize is the compressed size and not the actual size of the initial file.


Workflow
=========

After being uploaded, the IFC will be processed on our servers.

.. NOTE::
    The process takes from few minutes to an hour depending on the size of the file and the options activated.

You can follow the progress on the ``status`` field:


================  ===================  ===================================================================
status            Name of the status   Description
================  ===================  ===================================================================
P                  Pending             Your IFC will soon be processed
I                  In process          The process has started
C                  Completed           The process is complete and you can retrieve data from the API
E                  Error               The process has failed.
                                       It's more likely to be a problem on our side. 
                                       An alert is triggered and our team will fix it promptly.
================  ===================  ===================================================================




.. _IFC files: https://en.wikipedia.org/wiki/Industry_Foundation_Classes



.. seealso::

    See also :doc:`webhooks content </guide/api_webhooks>`
    
    .. include:: ../webhooks.rst
       :start-after: excerpt
       :end-before: endexcerpt