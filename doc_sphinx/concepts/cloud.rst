========
Cloud
========

.. 
    excerpt
        A cloud is a global space where your projects are hosted.
    endexcerpt

Concept
---------

A cloud is a set of :doc:`projects <projects>` sharing the same configuration. 
Each project contains your models, your Document Management System and BCFs.

Cloud administrators are also Projects admin by default, they can see every user in their cloud and change everyone's roles.

Cloud users can't see cloud collaborators. This means that a contractor on a project can't see every collaborator of the company.

References
------------

* GET ``/cloud``
* POST ``/cloud``
* GET ``/cloud/{cloud_pk}/user``
* GET ``/cloud/{cloud_pk}/user/{user_pk}``
* GET ``/cloud/{cloud_pk}/invitation``
* GET ``/cloud/{cloud_pk}/size``
* GET ``/cloud/{cloud_pk}/create-demo``


.. seealso:: 

    See also :ref:`api_onboarding_cloud`
