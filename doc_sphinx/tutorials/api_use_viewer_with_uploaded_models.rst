
======================================================
How can I use BIMData Viewer with my uploaded Models ?
======================================================

..
    excerpt
        How can I use BIMData Viewer with my uploaded Models ?
    endexcerpt

To open the Viewer, you need a Model and an Access Token.


You probably don't want to share the access token of your app: it has write access to everything in your Cloud.
We recommand create an Access Token for only one IFC, read-only or read/write.

To use them, your application needs the scope ``ifc:token_manage``


.. seealso::

    `See the API call to create an Access Token`_


If you want to be able to update the model information, set ``read_only`` to false.

.. note::
    
    The default duration is one hour. 


    If you want a longer or shorter token, you can specifies an expiration date in the ``field expires_at`` with the `iso-8601 format`_

.. substitution-code-block:: bash

    curl --request POST 'https://api-staging.bimdata.io/cloud/YOUR_CLOUD_ID/project/YOUR_PROJECT_ID/ifc/YOUR_IFC_ID/access_token' \
      --header 'Content-Type: application/json' \
      --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
      --data '{"read_only": true, "expires_at": "2020-02-11T00:00:00.000Z"}'

Then follow :doc:`the Viewer tutorial with your access token </tutorials/using_custom_viewer>` and your IDs to instanciate a viewer,

.. _See the API call to create an Access Token: api/index.html#createAccessToken
.. _iso-8601 format: https://www.iso.org/iso-8601-date-and-time-format.html