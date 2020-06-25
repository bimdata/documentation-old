:produit: dev

=============================
How-to get your Access Token
=============================

..
    excerpt
        The script regarding the Access Token
    endexcerpt


.. WARNING:: Pre-requisite: having created an application

    Look at the procedure to create an application, then come back here.
    After the application is created, you can retrieve it on the BIMData.io account manager, in the "Manage your application" screen.

Get your access token
======================

The Client ID and the Client Secret are the 2 elements that you need to get the Access Token of your application from the Authentication Server. You will need this Access Token for every call of the bimdata's API.



Python
^^^^^^^^

.. code-block:: python

    import requests

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
    }

    #Get the token
    response = requests.post("|iam_url|/auth/realms/bimdata/protocol/openid-connect/token", data=payload)
    access_token = response.json().get("access_token")

Curl
^^^^^^^^

.. code-block:: bash

    curl --request POST "|iam_url|/auth/realms/bimdata/protocol/openid-connect/token" \
      --header "Content-Type: application/x-www-form-urlencoded" \
      --data "grant_type=client_credentials&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET"


.. WARNING:: This API call doesn't accept JSON

    Be sure to use application/x-www-form-urlencoded encoding

.. seealso::

    See also :doc:`the API documentation </guide/api_guide>`


.. tip::

    Your user has no access to what your application created. To grant access to your user see :doc:`how-to share data with your app <api_share_data_app_platform>`
