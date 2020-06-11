=============================
Postman
=============================

..
    excerpt
        BIMData released a Postman Collection for you to enjoy and try our API in your usual software.
    endexcerpt

Postman is a powerful software letting you run HTTP requests against APIs.
BIMData released a Postman Collection for you to enjoy and try our API in your usual software.


Pre-requisites
===============

 * Have an account on BIMData Connect: ``client_id`` and ``client_secret`` are mandatory to request an Access Token.
 * Postman installed, it is supported `on Windows, Mac OS, and Linux <https://learning.getpostman.com/docs/postman/launching-postman/installation-and-updates/#supported-platforms>`_. There is even a Web-view (Chrome extension) if you do not want to use the desktop software. 

Steps
=======


1 - Get the Collection
------------------------

By clicking the Run in Postman! button, Postman launches the Collection directly.

.. image:: https://run.pstmn.io/button.svg
   :alt: Run in Postman!
   :target: https://app.getpostman.com/run-collection/3d3c0b2a685505934729

You can also use the direct sharing link to the BIMData's Examples collection: https://www.getpostman.com/collections/3d3c0b2a685505934729

.. note::
    
    If it's not installed on your computer, the Postman's software guides you with installation, according to your configuration.


2 - Set up an Environment
---------------------------

Follow the Postman documentation to create an Environment: https://learning.getpostman.com/docs/postman/environments-and-globals/manage-environments/
Create a new Environment by clicking the wheel icon [Manage environments] 

Then fill the following 3 variables with your data from BIMData Connect:
 
.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Variable name
     - Initial value / value
   * - client_id
     - {your client ID}
   * - client_secret
     - {your client secret}
   * - env
     - staging


**You are now ready to run requests in Postman on the BIMData's API.**

.. tip::

    Read Postman documentation to `discover what is a Postman Environment <https://learning.getpostman.com/docs/postman/environments-and-globals/intro-to-environments-and-globals/>`_


3 - Get your credentials
--------------------------

First of all, run the "Get Access Token" request. It will fill the acces_token value in your Environment.


4 - Run your first request
-----------------------------

Then to check your credentials and API access, run the "List my clouds" request.
The right-side panel shows you the JSON response, with your data.
