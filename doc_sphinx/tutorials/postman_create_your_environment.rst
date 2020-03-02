=======================================
How-to create your Postman environment
=======================================

.. 
    excerpt
        Create a Postman env to authenticate to the API.
    endexcerpt


Introduction
=============
To tryout our API and explore its capacities, we provide 2 Postman collections:

* The full API collection: https://documenter.getpostman.com/view/7460463/SzKTvyVR
* The BIMData's Examples collection: https://documenter.getpostman.com/view/7460463/SzKbLFKH

Pre-requisites
===============

* Create an application to get your ``client_id`` and ``client_secret``.

.. note::
    
    See :doc:`the tutorial about Create an application </tutorials/dev_create_an_application>`.

Create an environment in Postman
=======================================

Fields
---------

The fields you need to fill are:
cloud_id
cloud_demo_id (already set in our base environment)
client_id
client_secret
accessToken => filled when you run the Authentication request
baseUrl => next (already set in our base environment)
oAuthUrl => iam (already set in our base environment)

Read also
==========

The Postman documentation about environments 
The Postman documentation about variables