:orphan:
=================
Ifc Access Token
=================

When using an application without users (through `client_credentials` auth), you want to use BIMData Viewer without exposing your application Access Token.

You can create a temporary Access Token for only one IFC, read-only or read/write.

To use them, your application needs the scope `ifc:token_manage`

* You can create a token with endpoint: https://api-staging.bimdata.io/doc#/ifc/createAccessToken
* You revoke a token with endpoint: https://api-staging.bimdata.io/doc#/ifc/deleteAccessToken
* You can list all existing tokens for an IFC with endpoint: https://api-staging.bimdata.io/doc#/ifc/getAccessTokens