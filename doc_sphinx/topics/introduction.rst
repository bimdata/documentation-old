.. index::
   single: API, HTTP, introduction, bimdata
   module: __topics__
   module: topic

======================================
Introduction
======================================


This page will help you get started with bimdata. You'll be up and running in a jiffy!
Suggest Edits

Introduction
================

The Bimdata API is organized around `REST <https://en.wikipedia.org/wiki/Representational_state_transfer>`_. Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. We use built-in HTTP features, like HTTP authentication and HTTP verbs, which are understood by off-the-shelf HTTP clients. We support `cross-origin resource sharing <https://en.wikipedia.org/wiki/Cross-origin_resource_sharing>`_, allowing you to interact securely with our API from a client-side web application (though you should never expose your secret API key in any public website's client-side code).
JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.

URL
================


The API URL is **https://api-beta.bimdata.io**
All API requests must be made over HTTPS. Calls made over plain HTTP will respond a 302, redirecting to the same URL over HTTPS.


API Enpoint
================
``https://api-beta.bimdata.io``


Content-Type
================


Endpoints usually only accept ``application/json`` content type.
Endpoints used for files upload use ``application/x-www-form-urlencoded`` (aka form-data) content type.

Libraries
================


We're currently maintaining two external libraries in javascript and python. They are auto-generated from our OpenAPI file with swagger-codegen

    Table of Contents
    Introduction
    URL
    Content-Type
    Libraries
