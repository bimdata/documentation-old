============================
# Create your application
============================

Create an account on the https://login-staging.bimdata.io/ website. After the login step, go to "Manage your application" and fill the form in order the Create an Application.

You will choose a Name for your application, let's type **"Wonderful app"** in the field *Name*.
Select the **Confidential** option in the field *Client Type*.
Select the **code (Authorization Code Flow)** option in the field *Response Type*.

These settings will allow your app to communicate using a unique token access.
Other choices are useful to manage the access rights for every API call.
[block:callout]
{
  "type": "success",
  "body": "These fields may be edited later."
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Scope",
    "0-1": "lists every granted access for your application on the data",
    "1-0": "JWT Algorithm",
    "1-1": "lets you choose which algorithm is used to encode ID tokens",
    "2-0": "Redirect URIs",
    "2-1": "set the behavior of your application for each user action. It's a list of authorized URIs where the user can be redirected after the authorization process",
    "3-0": "Post Logout Redirect URIs",
    "3-1": "list of callback URIs when the user logs out from your application",
    "4-0": "Website URL",
    "4-1": "Your application's website",
    "5-0": "Terms URL",
    "6-0": "Logo Image",
    "5-1": "Terms of service of your application",
    "6-1": "Logo of your application"
  },
  "cols": 2,
  "rows": 7
}
[/block]


Let the other fields to their default value for now and submit the form. You will see 2 new pieces of information:  the Client ID and the Client Secret.


[block:callout]
{
  "type": "info",
  "body": "OAuth 2.0 scopes provide a way to limit the amount of access that is granted to an access token. For example, an access token issued to a client app may be granted READ and WRITE access to protected resources, or just READ access. You can implement your APIs to enforce any scope or combination of scopes you wish. So, if a client receives a token that has READ scope, and it tries to call an API endpoint that requires WRITE access, the call will fail.\n\nsource : [https://docs.apigee.com/api-platform/security/oauth/working-scopes\n](https://docs.apigee.com/api-platform/security/oauth/working-scopes)",
  "title": "About scopes"
}
[/block]
