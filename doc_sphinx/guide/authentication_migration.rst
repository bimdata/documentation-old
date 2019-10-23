===================================
Authentication migration
===================================

.. 
    excerpt
        The new Authentification process is slightly different, learn how to migrate.
    endexcerpt

The authentication migration is currently under progress. 
Your old credentials are still working with the new Authentication, however the association of the users credentials with their clouds is no longer provided.

.. warning:: 
    
   The previous authentication will no longer be available from 30th April 2019.


What's new?
===========

* The new authentication process no longer need your username nor your password.
* URL is not the same than the previous one.
* Grant type is now: 'client_credentials'

The new authentication is fully implementing OpenID Connect offering to the users a more secure authentication.
Additionally to that, respecting the OpenID Connect standard means more features such as authenticate users from your front or your back apps, emulate the user's actions and also create your own credentials.

Learn more `about the new authentication on the dedicated page`_.

.. _about the new authentication on the dedicated page: ../guide/authentication_bimdata_connect.html


Comparison of Requests
=========================

Comparing the old and new (current) requests and responses shows the similarities between the old and new authentications.

Old Authentication Request
---------------------------

The old request was a string payload with username and password in it.

.. substitution-code-block:: python

    import requests
    url = "|api_url|/oauth/v2/token/"
    payload = "client_secret=CLIENT_SECRET&client_id=CLIENT_ID&grant_type=password&username=my_user%40mail.com&password=passw0rd"
    response = requests.post(url, data=payload, headers=headers)


New Authentication Request
---------------------------

The new request takes a JSON payload.

.. substitution-code-block:: python

    import requests
    url = "|iam_url|/auth/realms/bimdata/protocol/openid-connect/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
    }

    response = requests.post(url, data=payload)


Comparison of Responses
===========================

Old Response
--------------

The old response contains a "refresh_token" property.

.. code:: json

    {
        "access_token": "ZeZr9oYxHspA99dSCo9uftaLaEHX1N",
        "expires_in": 36000,
        "token_type": "Bearer",
        "scope": "read write",
        "refresh_token": "MI8fx999PmcfdEDYntvBIKck999BuM"
    }


New Response
--------------

The new response has a more detailed scope.

.. code:: json

    {
        "access_token": "108a3781a1234a9d84a12345bd863d7c",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": "ifc:read
        ifc:write
        cloud:read
        cloud:manage
        document:read
        document:write"
    }

.. seealso::
    
    See also :doc:`the current Authentication process <authentication_bimdata_connect>`