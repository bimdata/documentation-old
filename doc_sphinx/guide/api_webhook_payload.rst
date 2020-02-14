:orphan:

=======================
Payload Details
=======================

.. note::

    ← Go back to :doc:`the Webhook guide <../guide/api_webhooks>`.

.. contents:: On this page:
   :local:
   :depth: 1


BCF Payload Details
===================

bcf.topic.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": Topic
    }

See `the Topic object definition <../api/index.html#definition-Topic>`_. 


bcf.topic.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": Topic
    }
    
See `the Topic object definition <../api/index.html#definition-Topic>`_. 


bcf.comment.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic_guid": topic_guid,
        "comment": Comment
    }

See `the Comment object definition <../api/index.html#definition-Comment>`_. 


bcf.comment.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic_guid": topic_guid,
        "comment": Comment
    }

See `the Comment object definition <../api/index.html#definition-Comment>`_. 


bcf.topic.full.creation
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": FullTopic
    }

See `the FullTopic object definition <../api/index.html#definition-FullTopic>`_. 


bcf.topic.full.update
------------------------------------------

.. code-block:: javascript

    {
        "project_id": project_id,
        "topic": FullTopic
    }

See `the FullTopic object definition <../api/index.html#definition-FullTopic>`_. 


IFC Payload Details
====================

ifc.process_update
------------------------------------------

.. code-block:: javascript

    {
        Ifc
    }

See `the Ifc object definition <../api/index.html#definition-Ifc>`_. 


Project Payload Details
=========================


project.creation
------------------------------------------

.. code-block:: javascript

    {
        Project
    }

See `the Project object definition <../api/index.html#definition-Project>`_. 


project.update
------------------------------------------

.. code-block:: javascript

    {
        Project
    }

See `the Project object definition <../api/index.html#definition-Project>`_. 


Document Payload Details
==========================


document.creation
------------------------------------------

.. code-block:: javascript

    {
        "document": Document,
        "project": Project,
    }

* See `the Project object definition <../api/index.html#definition-Project>`_. 
* See `the Document object definition <../api/index.html#definition-Document>`_. 


document.update
------------------------------------------

.. code-block:: javascript

    {
        "document": Document,
        "project": Project,
    }

* See `the Project object definition <../api/index.html#definition-Project>`_. 
* See `the Document object definition <../api/index.html#definition-Document>`_. 


.. seealso::

    See :doc:`the Webhook guide <../guide/api_webhooks>`.
