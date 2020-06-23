==========================================================
How can I share data between my app and BIMData Platform?
==========================================================

..
    excerpt
        How can I share data between my app and BIMData Platform?
    endexcerpt


You can invite your user in the Cloud you created with your app: `/api/index.html#inviteCloudUser </api/index.html#inviteCloudUser>`_

.. code-block:: bash
   :substitutions:

    curl --request POST '|api_url|/cloud/YOUR_CLOUD_ID/invitation' \
      --header 'Content-Type: application/json' \
      --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
      --data '{"email": "YOUR_EMAIL_ADDRESS", "redirect_uri": "https://platform.bimdata.io/cloud/YOUR_CLOUD_ID"}'

.. tip::

    Check if the Platform URL is the correct one for your Platform access.

You receive an email asking you to accept the invitation.
Once accepted, you can open the Platform and see the Cloud created by the application.

.. note::
    
    When your app needs to access data created on the Platform by a User: create the Cloud with the app and invite the User as an Admin to the Cloud.
    Then every data in this Cloud is accessible by your application.