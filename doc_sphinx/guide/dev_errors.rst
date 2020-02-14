.. index::
   single: errors, HTTP
   module: guide


===========
Errors
===========

.. 
    excerpt
        BIMData uses conventional HTTP response codes to indicate the success or failure of an API request. 
    endexcerpt

BIMData uses conventional HTTP response codes to indicate the success or failure of an API request. 

* Codes in the 2xx range indicate success.
* Codes in the 4xx range indicate an error from the client-side. Client-side has failed given the information provided (e.g., a required parameter was omitted, you don't have permission to access this resource, etc.).
* Codes in the 5xx range indicate an error with Bimdata's servers (these should be rare).

Some 4xx errors include an error code explaining the reported error:

400 Bad Request Response example
=================================

.. code-block:: json

    {
        "name": [
            "This field is required."
        ]
    }

.. seealso::
    
    See also :doc:`the API documentation </api/introduction>`