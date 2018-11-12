====================
Error codes
====================



HTTP Statuses Response Codes
=============================

============ ================================================================================================================================================================
Status Code	 Description
============ ================================================================================================================================================================
200 	     The request has succeeded.
201 	     The request has been fulfilled and has resulted in new resources created.
202 	     The request has been accepted for processing, and the processing has not been completed.
204 	     The server has successfully fulfilled the request, there is no content in the response body.
304 	     There was no new data to return. Typically used to indicate that the cached version of the response is still valid.
400 	     The request was invalid or cannot be otherwise served. Typical when there is a syntax error in the request. The response payload body provides details.
401 	     Missing or incorrect authentication credentials.
403 	     The request is understood, but it has been refused or access is not allowed. The response payload body provides details.
404 	     The requested resource does not exist. Sometimes, when it is prudent to hide the existence of a resource from an unauthorized client, a 403 error may be generated instead of this error.
406 	     An invalid format is specified in the request.
429 	     The application’s rate limit for the resource has been exceeded.
500 	     Indicates an error with Bimdata's servers (these should be rare).
502 	     API is down, or being upgraded.
============ ================================================================================================================================================================

