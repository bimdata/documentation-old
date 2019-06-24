==========================================
Process BCF data for Excel export
==========================================

.. 
    excerpt
        You want statistics about which Elements are the most commented with BCF.
    endexcerpt


You want statistics about which Elements are the most commented with BCF.
You have to export data about the commented elements, you want to produce Excel files to import to a stats software.
You will create a CSV file, each line is for an Element. 
Our API implements `the 2.1 version of the BCF specification`_


The column are: 

* Element Type
* Classification title
* Classification Notation
* Element UUID
* Topic GUID


Let's help you to achieve your goal.

.. note:: Performance

    For clarity reasons, the code shown below is not optimized.



Step 1 - Get all Topics from your Model
=======================================

First step, with a single endpoint, you get all the Topics attached to your Model, and the IFCs ID.
Iterate on topics and do another request to get the Viewpoints. 

.. tip:: API specs
    Explore the OpenAPI specification for the endpoint: |api_url|/doc?format=openapi


.. note:: 
    The BIMData's UI tools let you have only one Viewpoint by Topic. The API let you manage several.
    It's the reason you see `viewpoints[0]` line 13.

.. substitution-code-block:: python
   :linenos:

    url = f'|api_url|/bcf/2.1/projects/{project_pk}/topics'
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    for topic in response.json():
        #iterate on topics and do another request to get viewpoints
        url = f'|api_url|/bcf/2.1/projects/{project_pk}/topics/{topic["guid"]}/topic-viewpoints'
        response = requests.get(url, headers=headers)
        viewpoints = response.json()

        if not viewpoints: #no viewpoint found
            continue
        
        viewpoint = viewpoints[0]
        topic_guid = topic.get("guid")
        ifcs_list = topic.get("ifcs")

        #populate elements list
        elements = viewpoint["components"]["selection"]
        element_uuids = [element["ifc_guid"] for element in elements]



Step 2 - Get the Elements 
==========================

Then you iterate on the Viewpoint's elements, and in this loop on the IFCs to get the details for each element, such as classification.

.. warning::

    Some IFCs could not have the Element, in the case of multi-model BCF.


.. substitution-code-block:: python
   :linenos:

    allElements = []
    for element_uuid in element_uuids:
        for ifc_pk in ifcs_list:
            url = f'|api_url|/cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}'
            response = requests.get(url, headers=headers)

            #if there is no matching IFC, we continue with the next one
            if(response.status_code != 200):
                continue

            raw_element = response.json()
            for classification in raw_element["classifications"]:
                element = {
                    "type": raw_element["type"],
                    "classification_title": classification["title"],
                    "classification_notation": classification["notation"],
                    "uuid": element_uuid,
                    "topic_guid": topic_guid
                }
                allElements.append(element)


Step 3 - Write your file
=========================

For our example, this is the code you write:

.. substitution-code-block:: python
   :linenos:
    
    with open(f'exportComments_{project_pk}.csv', 'w', newline='') as csvfile:
            topicwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            topicwriter.writerow(["Element Type", "Classification", "Class. Notation", "UUID", "Topic GUID"]) #changeHeaders
            for oneElement in allElements:
                topicwriter.writerow([
                    oneElement["type"], 
                    oneElement["classification_title"], 
                    oneElement["classification_notation"], 
                    oneElement["uuid"], 
                    oneElement["topic_guid"]
                ])


You have now a CSV file Excel-compatible!

.. image:: /_images/tutorials/BIMdata_export_excel.png
   :scale: 100 %
   :alt: Screenshot of an Excel export of comments
   :align: center

The full script
=================

.. substitution-code-block:: python
   :linenos:

    import requests
    import csv

    cloud_pk = CLOUD_ID
    project_pk = PROJECT_ID
    headers = { 
        "Authorization": "Bearer ACCESS_TOKEN"
    }

    allElements = []

    url = f'|api_url|/bcf/2.1/projects/{project_pk}/topics'
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

    for topic in response.json():
        url = f'|api_url|/bcf/2.1/projects/{project_pk}/topics/{topic["guid"]}/topic-viewpoints'
        response = requests.get(url, headers=headers)
        viewpoints = response.json()
        if not viewpoints: 
            continue
        viewpoint = viewpoints[0]
        topic_guid = topic.get("guid")
        ifcs_list = topic.get("ifcs")

        elements = viewpoint["components"]["selection"]
        element_uuids = [element["ifc_guid"] for element in elements]

        for element_uuid in element_uuids:
            for ifc_pk in ifcs_list:
                url = f'|api_url|/cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}'
                response = requests.get(url, headers=headers)
                if(response.status_code != 200):
                    continue

                raw_element = response.json()
                for classification in raw_element["classifications"]:
                    element = {
                        "type": raw_element["type"],
                        "classification_title": classification["title"],
                        "classification_notation": classification["notation"],
                        "uuid": element_uuid,
                        "topic_guid": topic_guid
                    }
                    allElements.append(element)

    with open(f'exportComments_{project_pk}.csv', 'w', newline='') as csvfile:
            topicwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            topicwriter.writerow(["Element Type", "Classification", "Class. Notation", "UUID", "Topic GUID"])
            for oneElement in allElements:
                topicwriter.writerow([
                    oneElement["type"], 
                    oneElement["classification_title"], 
                    oneElement["classification_notation"], 
                    oneElement["uuid"], 
                    oneElement["topic_guid"]
                ])
        

You now have your data ready to be printed in a CSV file, or sent to your favorite Excel-file generator.


.. _the 2.1 version of the BCF specification: https://github.com/buildingSMART/BCF-API/tree/v2.1