==========================================================
How can I share data between my app and BIMData Platform ?
==========================================================

..
    excerpt
        How can I share data between my app and BIMData Platform ?
    endexcerpt


You can invite your user in the cloud you created with your app: /api/index.html#inviteCloudUser

.. code-block:: bash

    curl --request POST 'https://api-staging.bimdata.io/cloud/YOUR_CLOUD_ID/invitation' \
      --header 'Content-Type: application/json' \
      --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
      --data '{"email": "YOUR_EMAIL_ADDRESS", "redirect_uri": "https://platform-staging.bimdata.io/cloud/YOUR_CLOUD_ID"}'

You we'll receive an email asking you to accept the invitation.
Once accepted, you can open the platform an you'll see the cloud created by the application.