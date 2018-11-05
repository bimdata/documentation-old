.. index::
   single: documents; folders; 
   single: folder
   single: project
   module: core

================================
Folders & Documents
================================

The API exposes a complete set of methods to upload and manage documents.

* Folders
* Documents


Folders
=========

Every project is created with a root folder. It is the starting point to create a new folder or upload documents.

JSON
^^^^^

``https://api-beta.bimdata.io/cloud/1/project/1``

.. code-block:: javascript

    {
        "id": 1,
        "name": "my project",
        "cloud": {...},
        "status": "A",
        "created_at": "2017-12-01T10:09:54Z",
        "updated_at": "2018-02-21T17:07:25Z",
        "root_folder_id": 3,
    }


* If a folder is created without parent_id, it will be placed under the root folder.
* You can't create a loop with folders (a parent being itself or a loop including multiple folders).

References
------------

* GET /cloud/{cloud_pk}/project/{project_pk}/folder
* POST /cloud/{cloud_pk}/project/{project_pk}/folder
* GET /cloud/{cloud_pk}/project/{id}/tree

Documents
===========


Bimdata API allows you to upload any kind of file (IFC, office, images, binaries, ...). Those files are named "documents".
You can define in which folder you want to put the file using a parent_id.
Upload a document

File upload is one of the few API calls which does not use the application/json content-type. This call uses x-www-urlencoded with form-data.
The name of the file field must be "file", meaning you have to fire multiple calls if you want to upload many files.

cURL
^^^^^^^^^

.. code-block:: bash

    curl -X POST \
    'https://api-beta.bimdata.io/cloud/1/project/1/document' \
    -H 'authorization: Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N'
    -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
    -F name=my_custom_name \
    -F file=@/path/to/XXX.pdf

JavaScript
^^^^^^^^^^^

.. code-block:: javascript

    var fs = require("fs");
    var request = require("request");

    var options = { method: 'POST',
    url: 'https://api-beta.bimdata.io/cloud/1/project/1/document',
    headers:
    { 'authorization': 'Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' },
    formData:
    { name: 'my_custom_name',
        file:
        { value: 'fs.createReadStream("/path/to/XXX.pdf")',
            options: { filename: '/path/to/XXX.pdf', contentType: null } } } };

    request(options, function (error, response, body) {
    if (error) throw new Error(error);

    console.log(body);
    });


Python
^^^^^^^^^

.. code-block:: python

    import requests

    url = "https://api-staging.bimdata.io/cloud/1/project/1/document"

    headers = {
        'authorization': 'Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N',
    }

    payload = {
        'name': 'my_custom_name'
    }

    files = {'file': open('/path/to/XXX.pdf', 'rb')}

    response = requests.request("POST", url, data=payload, files=files, headers=headers)

    print(response.text)


Response
---------

.. code-block:: json

    {
        "id": 424,
        "parent": 1,
        "creator": 134,
        "project": "1",
        "name": "my_custom_name",
        "file_name": "XXX.pdf",
        "description": null,
        "file": "https://storage.gra3.cloud.ovh.net/v1/AUTH_b6a1c0b6b7c041d3a71d56f84ce25102/bimdata-staging-dev/cloud_1/project_1/XXX.pdf?temp_url_sig=311d34059bbebc87cd7f37de244bb6b62d114679&temp_url_expires=1527771256",
        "size": 175780,
        "created_at": "2018-05-31T12:24:16Z",
        "updated_at": "2018-05-31T12:24:16Z",
        "ifc_id": null,
        "parent_id": 1
    }


Download a document
-----------------------

Files are stored on OVH OpenStack Swift. You can download them using the URL returned. The URL is valid for 1 hour.

cURL
^^^^^^^^^

.. code-block:: bash

    curl -X GET \
    'https://storage.gra3.cloud.ovh.net/v1/AUTH_b6a1c0b6b7c041d3a71d56f84ce25102/bimdata-staging-dev/cloud_1/project_1/XXX.pdf?temp_url_sig=311d34059bbebc87cd7f37de244bb6b62d114679&temp_url_expires=1527771256'

Javascript
^^^^^^^^^^^

.. code-block:: javascript

    var request = require("request");

    var url = 'https://storage.gra3.cloud.ovh.net/v1/AUTH_b6a1c0b6b7c041d3a71d56f84ce25102/bimdata-staging-dev/cloud_1/project_1/XXX.pdf?temp_url_sig=311d34059bbebc87cd7f37de244bb6b62d114679&temp_url_expires=1527771256'

    var options = {
    method: 'GET',
    url: url,
    }

    request(options, function (error, response, body) {
    if (error) throw new Error(error);

    console.log(body);
    });

Python
^^^^^^^^^

.. code-block:: python

    import requests

    url = "https://storage.gra3.cloud.ovh.net/v1/AUTH_b6a1c0b6b7c041d3a71d56f84ce25102/bimdata-staging-dev/cloud_1/project_1/XXX.pdf?temp_url_sig=311d34059bbebc87cd7f37de244bb6b62d114679&temp_url_expires=1527771256"

    response = requests.request("GET", url)

    print(response.text)

References
--------------

* GET /cloud/{cloud_pk}/project/{project_pk}/document
* POST /cloud/{cloud_pk}/project/{project_pk}/document
