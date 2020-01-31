.. index::
   single: execution
   single: context
   single: projects
   module: core

==========
Projects
==========

.. 
    excerpt
        A Project is a place where IFC files and documents are stored.
    endexcerpt


Concept
=========

A project is a place where IFC files and documents are stored. IFC files and documents can be uploaded and organized, checkplans are defined.

A project is attached to a cloud and a cloud can host an infinite number of projects.

A project contains:
 * your models
 * your Document Management System
 * and BCFs.

.. note:: 

   A BCF is linked to a project, not a model.

A project member can see all other members, and admin member can add a user to the project.

References
================

* GET ``/user/projects``
* GET ``/cloud/{cloud_pk}/project``
* POST ``/cloud/{cloud_pk}/project``



.. seealso::

    See also :doc:`Getting Started </getting_started/developer_guided_tour>` to learn how-to setup your project.
    
    .. include:: /getting_started/developer_guided_tour.rst
       :start-after: excerpt
       :end-before: endexcerpt