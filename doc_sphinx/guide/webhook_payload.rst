:orphan:

=======================
Payload Details
=======================

BCF Payload Details
====================


bcf.topic.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": Topic
    }

Topic is https://developers-staging.bimdata.io/api/index.html#definition-Topic

bcf.topic.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": Topic
    }
    
Topic is https://developers-staging.bimdata.io/api/index.html#definition-Topic


bcf.comment.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic_guid": topic_guid,
        "comment": Comment
    }

Comment is https://developers-staging.bimdata.io/api/index.html#definition-Comment


bcf.comment.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic_guid": topic_guid,
        "comment": Comment
    }

Comment is https://developers-staging.bimdata.io/api/index.html#definition-Comment

bcf.topic.full.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": FullTopic
    }


FullTopic is https://developers-staging.bimdata.io/api/index.html#definition-FullTopic

bcf.topic.full.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": FullTopic
    }

FullTopic is https://developers-staging.bimdata.io/api/index.html#definition-FullTopic

IFC Payload Details
====================

ifc.process_update
------------------------------------------

.. code-block:: javascript

    {
        Ifc
    }

Ifc is https://developers-staging.bimdata.io/api/index.html#definition-Ifc

Project Payload Details
=========================

project.creation
------------------------------------------

.. code-block:: javascript

    {
        Project
    }
    
Project is https://developers-staging.bimdata.io/api/index.html#definition-Project

project.update
------------------------------------------

.. code-block:: javascript

    {
        Project
    }

Project is https://developers-staging.bimdata.io/api/index.html#definition-Project

Document Payload Details
==========================

document.creation
------------------------------------------

.. code-block:: javascript

    {
        "document": Document,
        "project": Project,
    }

Document is https://developers-staging.bimdata.io/api/index.html#definition-Document
Project is https://developers-staging.bimdata.io/api/index.html#definition-Project

document.update
------------------------------------------

.. code-block:: javascript

    {
        "document": Document,
        "project": Project,
    }
Document is https://developers-staging.bimdata.io/api/index.html#definition-Document
Project is https://developers-staging.bimdata.io/api/index.html#definition-Project
