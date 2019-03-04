.. index::
   single: cloud; context; user
   module: core

========
Cloud
========

.. 
    excerpt
        Find out more about a Cloud and Cloud users.
    endexcerpt

Concept
---------

A cloud is a global space where doc `projects`_ are hosted. A cloud is a workspace for your company. It also could be a personal playground.

Cloud administrators are also Projects admin by default, they can see every user in their cloud and change everyone's roles.

Cloud users can't see cloud collaborators. This means that a contractor on a project can't see every collaborator of the company.

Not many actions are available directly on clouds.

References
------------

* GET ``/cloud``
* POST ``/cloud``
* GET ``/cloud/{cloud_pk}/user``

.. _projects: projects.html
