:orphan:
=================
Ifc Access Token
=================

When using an application without Users (through `client_credentials` auth), you want to use BIMData Viewer without exposing your application Access Token.

You can create a temporary Access Token for only one IFC, read-only or read/write.

To use them, your application needs the scope `ifc:token_manage`

* You can create a token `with the createAccessToken endpoint`_
* You revoke a token `with the deleteAccessToken endpoint`_
* You can list all existing tokens for an IFC `with the getAccessTokens endpoint`_
.. seealso::

    See also :doc:`Create an application </cookbook/create_an_application>`


.. _with the createAccessToken endpoint: ../api/index.html#operation--cloud--cloud_pk--project--project_pk--ifc--ifc_pk--access_token-post
.. _with the deleteAccessToken endpoint: ../api/index.html#operation--cloud--cloud_pk--project--project_pk--ifc--ifc_pk--access_token--token--delete
.. _with the getAccessTokens endpoint: ../api/index.html#operation--cloud--cloud_pk--project--project_pk--ifc--ifc_pk--access_token-get