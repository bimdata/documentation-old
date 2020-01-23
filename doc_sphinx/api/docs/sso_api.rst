SSO API
=======

Les textes sont en bonne partie copiés/collés de
https://developers-staging.bimdata.io/guide/identity_providers.html
et de
https://developers-staging.bimdata.io/guide/invitations.html


BIMData supports many Identity Providers (BIMData Connect is an Identity provider) through Keycloak, an Open Source software backed by RedHat.

If you already own a user management system (Active Directory, LDAP, SAMLv2 or OpenId Connect), you may don’t want to use BIMData Connect. Services developed around BIMData (forked platform or any other app) can replace default BIMData Connect login with their own. Doing so, you can also manage the invitation process yourself, ie. to send custom invitation e-mails or to validate an invitation automatically without user consent.


There is not yet interfaces to configure your own Identity Provider with BIMData. You must contact us at support@bimdata.io if you want to use or try this feature.



By default, BIMData Connect manages invitations:
 * receives invitations from BIMData API
 * send a mail to the recipient
 * Suggest two choices to the user: Accept or Deny the invitation
 * Send the response to BIMData API


Use your own Identity Provider
------------------------------

If you use your own Identity Provider, you must manage invitations yourself (standing by the idea that it’s “Your users, your process”).

When you register an Identity Provider, you must define an Invitation URL where the invitation’s data will be sent. We send a bundle of data to this URL (see the details below in Example Request).

In addition to that, you need to give us a secret to sign invitation calls to guarantee the call is legit (sent by us and not by a malicious hacker). [See signature section]

When an invitation is created with inviteCloudUser [https://developers-staging.bimdata.io/api/index.html#inviteCloudUser] or inviteProjectUser [https://developers-staging.bimdata.io/api/index.html#inviteProjectUser], BIMData API saves the invitation with the status PENDING (P) and send a signal to your invitation URL.

```
curl -H "Content-Type: application/json" -X POST INVITATION_URL -d '{
  "id": 1,
  "client_id": "111111",
  "redirect_uri": "https://platform.bimdata.io/cloud/12/project/15",
  "cloud_name": "Awesome Cloud",
  "project_name": "Awesome Project",
  "cloud_role": 50,
  "project_role": 100,
  "email": "user@bimdata.io",
  "sender_provider_sub": "12345678-564798-8789-784563",
}'
```

The detail of the fields
-----------------------------

.. list-table::
   :header-rows: 1
   :widths:  10 25 65

   * - Name
     - Value example
     - Description
   * - id
     - `123`
     - The ID of the invitation
   * - client_id
     - `"111111"`
     - The ID of the application that made the call
   * - redirect_uri
     - `"https://platform.bimdata.io/cloud/12/project/15"`
     - The redirect URI defined in the invitation  
   * - cloud_name
     - `"Awesome Cloud"`
     - The name of the cloud. Usefull for email templating
   * - project_name
     - `"Awesome Project"`
     - The name of the project. Is the invitation is only in a cloud, the field is null
   * - cloud_role
     - `50`
     - The ID of the application that made the call
   * - project_role
     - `100`
     - The user status in the cloud of the invitation. 100 is Administrator, 50 is standard user, 25 is Guest
   * - email
     - `"user@bimdata.io"`
     - The email of the user
   * - sender_provider_sub
     - `"12345678-564798-8789-784563"`
     - The original (from your provider) OIDC sub or it's SAML v2 equivalent of the user who send the invitation.
       If the invitation was sent by an application, the field is null


Signature
---------

To avoid malicious calls, we sign the request with a hash serving as a client secret of your provider's application as explained here: https://developers-staging.bimdata.io/guide/webhook_signature.html (renommer en call_signatures ?)

If the invitation is sent again, you will receive the same JSON with the same id.



Message received
----------------

Once the message is received, you do whatever you need with it:

 * Send an e-mail to the receiver and let him accept or deny the invitation,
 * Automatically accept or deny the invitation,
 * Anything else.

Accept or deny an invitation
----------------------------

To accept or deny an invitation, see `Identity Provider in the API Reference`_
Only Identity Provider Applications can call these routes.

 * To accept an invitation (after user consent or automatically), see `acceptInvitation API Reference`_
 * To deny an invitation (after user consent or automatically), see `denyInvitation API Reference`_

If an admin user cancels an invitation, we send a call: ``DELETE {invitation_url}/{invitation_id}`` and we delete the invitation on our side, meaning the canceled invitation will no longer exist and can't be accepted or denied anymore.