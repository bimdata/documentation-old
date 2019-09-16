Webhooks
========

.. 
    excerpt
        Webhooks allow you to build automation around BIMData API.
    endexcerpt

Webhooks let you build automation around BIMData API. 
Your app can subscribe to certain events on BIMData API and when one event is triggered,
we'll send an HTTP POST payload to the configured URL.

Webhooks can be configured on a cloud. All projects of this cloud emits events.

Events
======

Each event corresponds to a set of actions.

======================== ==============================================================================
Event                     Triggered when... 
======================== ==============================================================================
bcf.topic.creation       a BCF Topic is created
bcf.topic.update         a BCF Topic is updated
bcf.comment.creation     a BCF comment is created
bcf.comment.update       a BCF comment is updated
bcf.topic.full.creation  a BCF Topic is created, send a FullTopic object 
bcf.topic.full.update    a BCF Topic is updated, send a FullTopic object 
ifc.process_update       the status of an IFC is changed (when it's processed) 
project.update           a project is updated 
project.creation         a project is created
======================== ==============================================================================


.. seealso::
    
    Read :doc:`the webhooks payload description <webhook_payload>`

Payload
=======

Every payload send by BIMData API looks like 
``{"event_name": event_name, "cloud_id": cloud_id, "data": payload}``

Where: 

 * ``event_name`` is the name of the triggered event
 * ``cloud_id`` is the cloud that triggered the event 
 * ``payload`` is the content of the event. 

It mostly uses the same serialization than the API Models.

Ping a webhook
==============

You can try if a webhook is well configured with https://api-next.bimdata.io/doc#/application/pingWebHook

Signature
=========

To verify if the Webhook is sent from BIMData API and not from a malicious user, we sign out HTTP POST requests. 
The signature is an HMAC hex digest generated using the ``sha256`` hash function 
and the secret as the HMAC key signing the body of the request.

This signature is sent over the ``x-bimdata-signature`` HTTP Header.

Here is a python example to check the signature:

.. substitution-code-block:: python

    import hmac
    import hashlib

    def is_signed(request):
        req_signature = request.META.get("HTTP_X_BIMDATA_SIGNATURE")
        if not req_signature:
            return False

        body_signature = hmac.new(
            WEBHOOK_SECRET.encode(), request.body, hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(req_signature, body_signature)

Authorizations
==============

API routes to manage Webhooks require the ``webhook:manage`` scope. 
As these calls don't involve a user, the app needs to be authorized itself 
on the Cloud and can't behave as a User.


.. seealso::
    
    See also :doc:`about IFC </concepts/ifc>`