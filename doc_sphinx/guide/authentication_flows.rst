====================
Authentication flows
====================

OpenID Connect has different authentication flows and you have to chose the one which fits your needs the best.


Authorization code flow
========================

This flow is designed to be used with apps using a backend with templating technologies.
It gives you an Access Token you can use directly to call the API and a Refresh Token you can use later to behave as a user even without the user actually using the application (ie: cron, asynchronous data processing)

You can forward the Access Token to the browser and let the browser directly call the BIMData API.
It this case, you need to implement a way to refresh the Access Token when it expires.

You can find more information here : https://rograce.github.io/openid-connect-documentation/explore_auth_code_flow
And you can find libraries helping you implementing it there: https://openid.net/developers/libraries/

.. highlights::
    Example: enrichment of your app's data with your own dataset.

Implicit flow
=============

This flow is designed to be used with apps without a backend like modiles apps or full javascript apps.
`Implicit flow` is the way when you don't need a back-end software. Everything is done in the user's browser.
It retrieves the access_token and can use it as you want. But when the token expires, you need the user to refresh it.

You can find a small example of implicit flow usage in a web browser here: https://github.com/bimdata/web-app-example
And you can find libraries helping you implementing it there: https://openid.net/developers/libraries/


.. highlights::

    Example: get the Access Token by the browser to use it directly after getting it.

.. highlights::
    Example2: reporting into the application of the user's actions


.. _Create an application process: ../cookbook/create_an_application.html
