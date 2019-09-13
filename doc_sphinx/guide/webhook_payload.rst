:orphan:

=======================
Payload Details
=======================

When an object is described with an UpperCamelCase name, it refers to the model of the same name in https://api-next.bimdata.io/doc

BCF Payload Details
====================


bcf.topic.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": Topic
    }

bcf.topic.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": Topic
    }

bcf.comment.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic_guid": topic_guid,
        "comment": Comment
    }

bcf.comment.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic_guid": topic_guid,
        "comment": Comment
    }

bcf.topic.full.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": FullTopic
    }

bcf.topic.full.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": FullTopic
    }


IFC Payload Details
====================

ifc.process_update
------------------------------------------

.. code-block:: javascript

    {
        Ifc
    }


Project Payload Details
=========================

project.creation
------------------------------------------

.. code-block:: javascript

    {
        Project
    }

project.update
------------------------------------------

.. code-block:: javascript

    {
        Project
    }


Document Payload Details
==========================

document.creation
------------------------------------------

.. code-block:: javascript

    {
        "document": Document,
        "project": Project,
    }

document.update
------------------------------------------

.. code-block:: javascript

    {
        "document": Document,
        "project": Project,
    }

