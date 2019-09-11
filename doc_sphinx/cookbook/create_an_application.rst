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

These settings allow your app to communicate using a unique Token Access.
Other choices are useful to manage the access rights for every API call.

Response Type
==============

See the two Types of Auth to learn more about the Response Type.

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
   * - Scopes
     - lists every granted access for your application on the data. 
       `See the Scopes documentation content <../concepts/scopes.html>`_ to learn more.
   * - Redirect URIs
     - determines where the authorization server sends a response to your app.
       It's a list of authorized URIs where the user can be redirected after the authorization process


Let the other fields to their default value and submit the form.
You created your first application.

You will see 2 new pieces of information: the Client ID and the Client Secret.
This Client ID and Client Secret are mandatory to build your application.

.. seealso::

    See also :doc:`about Security </guide/security>`