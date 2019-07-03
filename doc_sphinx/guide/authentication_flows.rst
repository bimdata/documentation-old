====================
Authentication flows
====================

OpenID Connect has different authentication flows and you have to choose the one which fits your needs the best.


Authorization code flow
========================

This flow is designed to be used with apps using a backend with templating technologies.
It gives you an Access Token you can use directly to call the API and a Refresh Token you can use later to behave as a user even without the user actually using the application (ie: cron, asynchronous data processing).

You can forward the Access Token to the browser and let the browser directly call the BIMData API.
It this case, you need to implement a way to refresh the Access Token when it expires.

.. note:: More information and libraries
   
   - Find more information on this Github repo: https://rograce.github.io/openid-connect-documentation/explore_auth_code_flow .
   - Find libraries helping you with the implementation: https://openid.net/developers/libraries/.

Usage example
--------------

* **Example:** enrichment of your app's data with your own dataset

Implicit flow
=============

This flow is designed to be used with apps without a backend like mobiles apps or full javascript apps.

``Implicit flow`` is the way when you don't need a back-end software. Everything is done in the user's browser.
It retrieves the access_token and can use it as you want. But when the token expires, you need the user to refresh it.

.. note:: Example and libraries
    
    - Find an example of implicit flow usage in a web browser on our's Github example repository: https://github.com/bimdata/web-app-example .
    - Find libraries helping you with the implementation: https://openid.net/developers/libraries/.


Usage examples
---------------

* **Example:** get the Access Token by the browser to use it directly after getting it
* **Example2:** reporting into the application of the user's actions


.. _Create an application process: ../cookbook/create_an_application.html
