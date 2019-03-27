=========================
Create your application
=========================

.. 
    excerpt
        How-To create your application on BIMData Connect
    endexcerpt

**How-To create your application on BIMData Connect**

Create an account on the |bimdata_connect| website. After the login step, go to "Manage your application" screen and fill the form to Create an Application.

You will choose a *Name* for your application, let's type **"Wonderful app"** in the field *Name*.

.. Note::
    All the fields may be edited later.

Select the **Confidential** option in the field *Client Type*.
Select the **code (Authorization Code Flow)** option in the field *Response Type*.

These settings allow your app to communicate using a unique Token Access.
Other choices are useful to manage the access rights for every API call.

Response Type
==============

See the three Types of Auth to learn more about the Response Type.

In the field *Redirect URIs*, set at least the value ``http://localhost``: for now, you want your brand new application to receive any response.

Fields description
====================

.. list-table:: Fields description
   :header-rows: 1
   :widths: 10 90

   * - Field name
     - Description
   * - Name
     - sets the name of your application. This name will be shown to the Users you will invite.
   * - Client Type
     - sets the confidentiality of your application's credentials     
           - A confidential client is an application that is capable of keeping a client password confidential to the world.
           - A public client is an application that is not capable of keeping a client password confidential.
           - `See the Tutorial made by Jenkov <http://tutorials.jenkov.com/oauth2/client-types.html>`_ for more explanations.
   * - Response Type
     - sets the way of authenticating, see the Authentication documentation content to learn more.
   * - Scopes
     - lists every granted access for your application on the data. 
       `See the Scopes documentation content <../concepts/scopes.html>`_ to learn more.
   * - JWT Algorithm
     - lets you choose which algorithm is used to encode ID tokens
   * - Redirect URIs
     - determines where the authorization server sends a response to your app.
       It's a list of authorized URIs where the user can be redirected after the authorization process
   * - Post Logout Redirect URIs
     - list of callback URIs when the user logs out from your application
   * - Website URL
     - Your application's website, if applicable. Visible on the BIMData Connect platform to users.
   * - Terms URL
     - Terms of service of your application, if applicable. Visible on the BIMData Connect platform to users.
   * - Logo Image
     - Logo of your application, if applicable. Visible on the BIMData Connect platform to users.

Let the other fields to their default value and submit the form.
You created your first application.

You will see 2 new pieces of information: the Client ID and the Client Secret.
This Client ID and Client Secret are mandatory to build your application.