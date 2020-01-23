The BCF API
===========

BIMData implements the BCF API v2.1 as defined by buildingSMART (https://github.com/buildingSMART/BCF-API)

BIMdata adds some feature to the standard to add functionalities, simplify the development or reduce the network usage:

  * You can export BCF created in the API in the BCFxml format (https://developers-staging.bimdata.io/api/index.html#downloadBcfExport)

  * A new route named full-topic allows you to retrieve all the data of a BCF topic in a single API call (https://developers-staging.bimdata.io/api/index.html#getFullTopic)

  * In the BCF API standard, there is no direct link between a topic and images of this topic (images of comments are shown as topic's images). We created a route to extract only images of the topic and not images from comments (https://developers-staging.bimdata.io/api/index.html#getTopicViewpoints)

Explore the API: https://developers-staging.bimdata.io/api_playground/bcf_endpoint.html


The Collaboration API
=====================

You can create clouds, projects, invite users, manage their rights and use the Document Management System.

Explore the API: https://developers-staging.bimdata.io/api_playground/collaboration_endpoint.html


Clouds
------

A cloud is a set of projects sharing the same configuration. Only an admin user (see users section) can change the configuration.
After creating your app, the first task you may want to do is create a cloud.

Clouds created on the BIMData Platform are own by the platform itself. That means the app you just created doesn't have access to these clouds. If you want to access to your Platform Data from your app, see [How can I share data between my app and BIMData Platform ?]



Projects
--------
A project is a container. It contains users, a DMS, IFC files, and can contain projects (recursively).

Recursive projets
^^^^^^^^^^^^^^^^^
You can create a subproject (https://developers-staging.bimdata.io/api/index.html#createProject) by using the parent_it field. All the related projects must be in the same cloud.

Each project has its own DMS, own users, own models, there is no data shared between parents and children projects.
A user can be in a child project without being in the parent. In this case, the user won't see the parent and the child will appear at the top level of projects. A user can have different roles in a parent and their children.



Users
-----
A user may be in one or many clouds and in one or many projects in each cloud.
A user can either be a cloud user (https://developers-staging.bimdata.io/api/index.html#definition-CloudRole with ROLE = 50) or a cloud administrator (role = 100).
A cloud administrator:
  * can invite other cloud admins
  * is by default an admin of all projects
  * can create projects
  * can see the members of the cloud

A cloud user:
  * can only see the cloud he's a member of
  * can see the list of cloud administrators

A user can be a project admin (https://developers-staging.bimdata.io/api/index.html#definition-ProjectRole with ROLE = 100), a project user (role = 100) or a project guest (role = 25)

A project admin:
  * can invite other people in the project
  * can change the project's users role
  * can kick a user from the project
  * do what a project user can do

A project user can:
  * upload documents in the DMS
  * upload IFC models
  * read IFC data
  * update IFC data (it won't update the original IFC file)
  * delete files or models
  * do what a project guest can do

A project guest can:
  * see the member of the project
  * read and download the documents in the DMS
  * See IFC data
  * Leave the project

Invitation process
------------------
Invitations in a cloud or a project are done through the email address od the person.
The person won't be directly added in the project but will receive an email:
  If there is no BIMData account attached to this address, the email will redirect the user to the account creation then to accept the invitation
  If there is a BIMData account, the email will redirect the user to accept the invitation.
  [screen des emails ?]

When a user accepts the invitation, it will be added to the corresponding cloud and project.
For a project invitation, the person is automatically added to the corresponding cloud as a standard user.

You can override this process if you use your own SSO (see SSO API).



DMS
---
The DMS (for Document Management System) is a place where you can create folders, upload files, and move or delete them.
You can upload any kind of file. If the file is an IFC model (.ifc or .ifczip extension), it will be processed by BIMData.

Files are stored on the OVH Object Storage based on OpenStack Swift.
The API doesn't send directly the files in the JSON responses (except for the BCF API to comply with the standard), it sends a URL to download the file. This URL is signed and valid for 1 hour. After that, The URL with respond with an error.