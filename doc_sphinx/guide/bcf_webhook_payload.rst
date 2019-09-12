:orphan:

=======================
BCF Webhook
=======================

When an object is described with an UpperCamelCase name, it refers to the model of the same name in https://api-next.bimdata.io/doc

BCF Payload Details
====================


bcf.topic.creation
------------------------------------------

.. code-block:: json

    {
        "project_id": project_id,
        "topic": Topic
    }

bcf.topic.update
------------------------------------------

.. code-block:: json

    {
        "project_id": project_id,
        "topic": Topic
    }

bcf.comment.creation
------------------------------------------

.. code-block:: json

    {
        "project_id": project_id,
        "topic_guid": topic_guid,
        "comment": Comment
    }

bcf.comment.update
------------------------------------------

.. code-block:: json

    {
        "project_id": project_id,
        "topic_guid": topic_guid,
        "comment": Comment
    }

bcf.topic.full.creation
------------------------------------------

.. code-block:: json

    {
        "project_id": project_id,
        "topic": FullTopic
    }

bcf.topic.full.update
------------------------------------------

.. code-block:: json

    {
        "project_id": project_id,
        "topic": FullTopic
    }

    ## IFC

ifc.process_update
------------------------------------------

.. code-block:: json

    {
        Ifc
    }

    ## Project

project.creation
------------------------------------------

.. code-block:: json

    {
        Project
    }

project.update
------------------------------------------

.. code-block:: json

    {
        Project
    }

document.creation
------------------------------------------

.. code-block:: json

    {
        "document": Document,
        "project": Project,
    }

document.update
------------------------------------------

.. code-block:: json

    {
        "document": Document,
        "project": Project,
    }

