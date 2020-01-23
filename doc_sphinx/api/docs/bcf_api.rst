The BCF API
===========

BIMData implements the BCF API v2.1 as defined by buildingSMART (https://github.com/buildingSMART/BCF-API)

BIMdata adds some feature to the standard to add functionalities, simplify the development or reduce the network usage:

  * You can export BCF created in the API in the BCFxml format (https://developers-staging.bimdata.io/api/index.html#downloadBcfExport)

  * A new route named full-topic allows you to retrieve all the data of a BCF topic in a single API call (https://developers-staging.bimdata.io/api/index.html#getFullTopic)

  * In the BCF API standard, there is no direct link between a topic and images of this topic (images of comments are shown as topic's images). We created a route to extract only images of the topic and not images from comments (https://developers-staging.bimdata.io/api/index.html#getTopicViewpoints)

Explore the API: https://developers-staging.bimdata.io/api_playground/bcf_endpoint.html
