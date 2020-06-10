=========
Filters
=========

..
    excerpt
        Many API end-points allow filtering.
    endexcerpt


Many API endpoints allow filtering.

See all the available filters by exploring the :doc:`Playground </api_playground/index>`.

Examples
=========

Let's use the resource IFC and the endpoint: ``/cloud/{cloud_pk}/project/{project_pk}/ifc``.

The response list only includes _completed_ IFCs (see :doc:`the IFC guide in our documentation </guide/concepts/ifc>` to learn about ``status``).
You can combine several filters. Elements matching **all combined filters** are returned.


.. IMPORTANT::

    Filtering is an **AND** operation.


.. note::

    No **OR** operation is supported in this version.


.. content-tabs::

   .. tab-container:: cURL
        :title: cURL

         .. code-block:: bash

            curl -X GET \
            '|api_url|/cloud/1/project/1/ifc?status=C' \
            -H 'Authorization: Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N' \
            -H 'Content-Type: application/json' \

   .. tab-container:: py
        :title: Python

         .. code-block:: python

            import requests

            url = "|api_url|/cloud/1/project/1/ifc"

            querystring = {"status":"C"}

            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer ZeZr9oYxHspA8OdSCo9uftaLaEHX1N",
                }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)

   .. tab-container:: javascript
        :title: JavaScript

         .. code-block:: javascript

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

.. seealso::

    Try other request and learn about the API on :doc:`the API documentation </guide/api_guide>`

