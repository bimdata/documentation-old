:orphan:
==================================
Webhook and Invitation signature
==================================

Signature
=========

To verify if the Webhook is sent from BIMData API and not from a malicious user, we sign out HTTP POST requests. 
The signature is an HMAC hex digest generated using the ``sha256`` hash function 
and the secret as the HMAC key signing the body of the request.

This signature is sent over the ``x-bimdata-signature`` HTTP Header.

Here is a python example to check the signature:

.. code-block:: python

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

.. seealso::

    View :doc:`the Webhook guide <../guide/api_webhooks>`.