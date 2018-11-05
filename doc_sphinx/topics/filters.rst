.. index::
   single: filters
   module: __topics__
   module: topic


=========
Filters
=========

Many API end-points allow filtering.
You can find information about available filters in the Swagger doc.

Exemples
=========

``/cloud/{cloud_pk}/project/{project_pk}/ifc``

cURL
=========

.. code-block:: bash

    curl -X GET \
    'https://api-staging.bimdata.io/cloud/1/project/1/ifc?status=C' \
    -H 'Authorization: Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N' \
    -H 'Content-Type: application/json' \

Python
=========

.. code-block:: python

    import requests

    url = "https://api-staging.bimdata.io/cloud/1/project/1/ifc"

    querystring = {"status":"C"}

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


Javascript
===========

.. code-block:: javascript

    var request = require("request");

    var options = { method: 'GET',
    url: 'https://api-staging.bimdata.io/cloud/1/project/1/ifc',
    qs: { status: 'C' },
    headers:
    { Authorization: 'Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N',
        'Content-Type': 'application/json',
    }
    };

    request(options, function (error, response, body) {
    if (error) throw new Error(error);

    console.log(body);
    });

The response list will only include completed IFCs (see `IFC <core_ressources/ifc>`_)

You can combine several filters. Elements matching all combined filters will be returned. (Filtering is an AND operation.)


.. note::

    No OR operation is supported in this version.
