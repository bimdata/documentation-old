:orphan:

====================
Error codes details
====================

.. 
    excerpt
        Find error messages for your users 
    endexcerpt

BIMData's API uses classical HTTP status code for the responses.
Here is a list of the messages with the HTTP status


HTTP Statuses Response Codes
=============================

============ ======================================================================================================================
Status Code	 Description
============ ======================================================================================================================
200 	     The request has succeeded.
201 	     The request has been fulfilled and has resulted in new resources created.
202 	     The request has been accepted for processing, and the processing has not been completed.
204 	     The server has successfully fulfilled the request, there is no content in the response body.
304 	     There was no new data to return. Typically used to indicate that the cached version of the response is still valid.
============ ======================================================================================================================

Error Codes
=============================

============ ========================================================================================================================================================================================================
Status Code	 Description
============ ========================================================================================================================================================================================================
400 	     The request was invalid or cannot be otherwise served. Typical when there is a syntax error in the request. A required field is missing in the body
401 	     The authentication failed. Your token may be expired, missing or malformed
403 	     You don't have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource.
404 	     The resource does not exist or you don't have the right to see if the resource exists
406 	     An invalid format is specified in the request.
429 	     The application’s rate limit for the resource has been exceeded.
500 	     Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we'll look at it shortly.
502 	     API is down, or being upgraded.
============ ========================================================================================================================================================================================================

.. seealso::
    
    See also :doc:`the API documentation </guide/api_guide>`