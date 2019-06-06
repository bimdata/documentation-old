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

.. substitution-code-block:: python

    import requests

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
    }

    #Get the token
    response = requests.post("|bimdata_connect|/token", data=payload)
    access_token = response.json().get("access_token")

Curl
^^^^^^^^

.. substitution-code-block:: bash

    curl --request POST "https://connect-next.bimdata.io/token" \
      --header "Content-Type: application/x-www-form-urlencoded" \
      --data "grant_type=client_credentials&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET"


.. WARNING:: This call doesn't accept json

    Be sure you use application/x-www-form-urlencoded encoding
