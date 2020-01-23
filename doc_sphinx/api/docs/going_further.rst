===================
Going further
===================

.. contents::

How can I share data between my app and BIMData Platform ?
==========================================================

You can invite your user in the cloud you created with your app: https://developers-staging.bimdata.io/api/index.html#inviteCloudUser

.. code-block:: bash

    curl --request POST 'https://api-staging.bimdata.io/cloud/YOUR_CLOUD_ID/invitation' \
      --header 'Content-Type: application/json' \
      --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
      --data '{"email": "YOUR_EMAIL_ADDRESS", "redirect_uri": "https://platform-staging.bimdata.io/cloud/YOUR_CLOUD_ID"}'

You we'll receive an email asking you to accept the invitation.
Once accepted, you can open the platform an you'll see the cloud created by the application.




How can I use BIMData Viewer with my uploaded models ?
======================================================

To open the viewer, you need a model and an access token.
You probably don't want to share the access token of your app: it has write access to everything in your cloud.
We recommand create an access token for only one IFC, read-only or read/write.

To use them, your application needs the scope ifc:token_manage

Create an access token (https://developers-staging.bimdata.io/api/index.html#createAccessToken)
If you want to be able to update the model information, set read_only to false.
The default duration is one hour. If you want a longer or shorter token, you can specifies an expiration date in the field expires_at with the iso-8601 format [link vers le format]

.. code-block:: bash

    curl --request POST 'https://api-staging.bimdata.io/cloud/YOUR_CLOUD_ID/project/YOUR_PROJECT_ID/ifc/YOUR_IFC_ID/access_token' \
      --header 'Content-Type: application/json' \
      --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
      --data '{"read_only": true, "expires_at": "2020-02-11T00:00:00.000Z"}'

Then follow the Viewer tutorial with your access token and your IDs to instanciate a viewer [link vers viewer tuto]


The Collaboration API
=====================

BIMData have many features useful to manage Projects and their users.

