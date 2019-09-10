===================================
Use-case: BCF in the blockchain
===================================

..
    excerpt
        Discover why BCF comments stored in a blockchain
    endexcerpt

Purpose
=======

Trace BCF history to know who handles the responsibility in case of conflict or request.

What was done?
==============

The blockchain in this use-case is to certify the order and authenticity of each BCF comment. 
The company needs it in case of any legal request to assess who is responsible for the breach. 
The blockchain part is not detailed here.

The BCF Server is set. Users fill it with BCF comments. 
Meanwhile, a listener catches them and write the BCF paired with a hash of the Model in a blockchain.
The listener is built using the Webhooks, through the “bcf.topic.creation” event.

This process is incorporated into BIMData Viewer via a custom BCF plug-in.

.. image:: /_images/use_cases/bcf_in_blockchain.png
   :scale: 50%
   :alt: BCF in blockchain
   :align: center

.. note::

    See more about :doc:`Webhooks <../guide/webhooks>`


