===========
The BCF API
===========

BIMData implements the standard BCF API v2.1 as defined by buildingSMART (https://github.com/buildingSMART/BCF-API)

BIMData, however, adds some features to the standard expanding functionalities, simplifying the development or reducing the network usage:

 * You can export BCF comments created in the API in the BCFxml format (See the `downloadBcfExport endpoint </api/index.html#downloadBcfExport)`_
 * A new route named `full-topic` allows you to retrieve all the data of a BCF topic using a single API call (See the `getFullTopic endpoint </api/index.html#getFullTopic>`_)
 * In the BCF API standard, there is no direct link between a topic and images of this topic (images of comments are shown as topic's images). We created a route to extract only images of the topic and not images from comments (See `the getTopicViewpoints endpoint </api/index.html#getTopicViewpoints>`_)

.. seealso:: 

    :doc:`Explore the API <api_playground/bcf_endpoint>`