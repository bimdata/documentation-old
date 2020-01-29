:orphan:
=================
IFC Access Token
=================

When using an application without Users (through `client_credentials` auth), you want to use BIMData Viewer without exposing your application Access Token.

You can create a temporary Access Token for only one IFC, read-only or read/write.

To use them, your application needs the scope `ifc:token_manage`

* You can create a token `with the createAccessToken endpoint`_
* You revoke a token `with the deleteAccessToken endpoint`_
* You can list all existing tokens for an IFC `with the getAccessTokens endpoint`_
* You can `retrieve one token`_ created for a given Model with the getAccessToken endpoint


.. seealso::

    See also :doc:`Create an application </cookbook/create_an_application>`

.. _with the createAccessToken endpoint: ../api/index.html#createAccessToken
.. _with the deleteAccessToken endpoint: ../api/index.html#deleteAccessToken
.. _with the getAccessTokens endpoint: ../api/index.html#getAccessTokens
.. _retrieve one token: ../api/index.html#getAccessToken
