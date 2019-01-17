===================================
Authentication migration
===================================

The authentication migration is currently under progress. 
Your old credentials are still working with the new Authentication, however the association of the users credentials with their clouds is no longer provided.

.. warning:: 
    
   The previous authentication will no longer be available from 30th April 2019.


What's new?
===========

* The new authentication process no longer need your username nor your password.
* URL is not the same than the previous one.
* Grant type is now: 'client_credentials'

The new authentication is fully implementing and respecting oAuth 2.0 offering to the users a more secure authentication.
Additionally to that, respecting the oAuth 2.0 standard means more features such as 
authenticate users from your front or your back apps, emulate the user's actions and also create your own credentials.

Learn more `about the new authentication on the dedicated page`_.

.. _about the new authentication on the dedicated page: ../topics/authentication_bimdata_connect.html
