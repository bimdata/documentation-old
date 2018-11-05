.. index::
   single: errors, HTTP
   module: __topics__
   module: topic


===========
Errors
===========

Bimdata uses conventional HTTP response codes to indicate the success or failure of an API request. In general: codes in the 2xx range indicate success.
Codes in the 4xx range indicate an error from the client-side, client-side has failed given the information provided (e.g., a required parameter was omitted, you don't have permission to access this resource, etc.).
Codes in the 5xx range indicate an error with Bimdata's servers (these should be rare).

Some 4xx errors include an error code explaining the reported error:

400 Bad Request Response example
=================================

.. code-block:: json

    {
        "name": [
            "This field is required."
        ]
    }
