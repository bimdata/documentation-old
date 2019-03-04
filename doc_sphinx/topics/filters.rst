.. index::
   single: filters
   module: topics


=========
Filters
=========

.. 
    excerpt
        Many API end-points allow filtering.
    endexcerpt

Many API end-points allow filtering.
See available filters in the `Swagger doc`_.

Examples
=========

Let use the resource IFC: ``/cloud/{cloud_pk}/project/{project_pk}/ifc``

The response list will only include completed IFCs (see `IFC`_).
You can combine several filters. Elements matching all combined filters will be returned. 


.. IMPORTANT::
    Filtering is an AND operation.


.. note::

    No OR operation is supported in this version.


cURL
=========

.. substitution-code-block:: bash

    curl -X GET \
    '|api_url|/cloud/1/project/1/ifc?status=C' \
    -H 'Authorization: Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N' \
    -H 'Content-Type: application/json' \

Python
=========

.. substitution-code-block:: python

    import requests

    url = "|api_url|/cloud/1/project/1/ifc"

    querystring = {"status":"C"}

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


Javascript
===========

.. substitution-code-block:: javascript

    var request = require("request");

    var options = { method: 'GET',
    url: '|api_url|/cloud/1/project/1/ifc',
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






.. _Swagger doc: https://api-beta.bimdata.io/doc
.. _IFC: concepts/ifc.html