==================
Users Management
==================

There is currently 3 roles defined for Users.
Each User has a Role, and each User belongs to a Project.

Roles
=====

Users can have this Roles:

* admin
* user
* guest

Constant values in API
-----------------------

Using the API, there are constant values associated to roles. 
See `the User endpoint`_ to learn about the usage.

.. note::
    
    These constants are only used in API.

When checking User's role through the API, the values are:

* Cloud role's values
   * admin: 100
   * user: 50

* Project role's values
   * admin: 100
   * user: 50
   * guest: 25


User in the Cloud
==================

Every User in the Cloud is linked to a Project.

Admin 
-------------

A cloud Admin can see every other member of the Cloud, can invite other Users as admin in the Cloud.

By default, the cloud Admin has admin rights on every project on the Cloud.

A cloud admin can ban any User from the Cloud.

.. warning::

    Ban a User exclude the User from all Projects of the Cloud. 

Member 
---------------

A Cloud member is at least a member of one Project.

User in the Project
===================

Any User in any Project can read the user list and see the other users of the project.


Admin 
-------------

A Project admin can invite Users to the Project.

.. note:: 

    The User is implicitly invited in the Cloud.

The Project admin manages the Roles of the Users: the admin car add, edit or delete Roles.


Member 
----------------

Can read and write EDM, model, and BCF.

Guest 
----------------

Can read-only : EDM, models, BCF and write BCF content.



.. _the User endpoint: |api_url|/doc#/user/getSelfUser