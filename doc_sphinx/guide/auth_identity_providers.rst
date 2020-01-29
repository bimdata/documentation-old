==================
Identity Providers
==================

.. 
    excerpt
        Log in BIMData with your own Active Directory, LDAP or OpenID Connect service
    endexcerpt

BIMData supports many Identity Providers (BIMData Connect is an Identity provider) through `Keycloak`_, an Open Source software backed by RedHat.

If you own your user management system (Active Directory, LDAP, SAMLv2 or OpenId Connect), you don't want to use BIMData Connect.
Services developed around BIMData (forked platform or any other app) can replace default BIMData Connect login with their own.
Doing so, you can also manage the :doc:`invitation process <../guide/invitations>` yourself, ie. to send custom invitation e-mails or to validate an invitation automatically without user consent. 

.. note::
    
    For more information about how to set up an Identity Provider, contact us at support@bimdata.io.

.. seealso:: 

     See :doc:`the Invitation process documentation <../guide/invitations>`.

.. _Keycloak: https://www.keycloak.org