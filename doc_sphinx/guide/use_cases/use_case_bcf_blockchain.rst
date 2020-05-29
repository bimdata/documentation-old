===================================
Use-case: BCF in the blockchain
===================================

..
    excerpt
        Discover why BCF comments are stored in a blockchain
    endexcerpt


Accountability is important in every BIM project. In case of conflict, or to answer preventively any request.

Even the BCF comments are timestamped in our BCF repository, 
one of the blockchain specificity by design is to let the sequence be trusted, as well as the reliable of every BCF comment as a block of the chain. 

The blockchain serves a trust purpose.

.. note::
    
    The blockchain part is not detailed here.

Purpose
=======

Trace BCF history to know who handles the responsibility.

What was done?
==============

The blockchain usage here is to certify the order and authenticity of each BCF comment. 
The company needs it in case of any legal request to assess who is responsible for the breach. 
The BCF Server is set up. Users comment Models using BCF comments and fill the server database with BCF comments. 
A listener has been plugged on the "create a new BCF comment" event.

.. note::
     
     The listener is built using the Webhooks, through the “bcf.topic.creation” event.


The listener catches every new BCF comment and then writes the BCF in a blockchain, paired with a hash of the Model to ensure the integrity of the block.
This process of recording BCF comment in a blockchain is incorporated into BIMData Viewer using a custom-made BCF plug-in.



.. image:: /_images/use_cases/bcf_in_blockchain.png
    :align: center
    :alt: Schematic process of BCF in the blockchain

.. tip::

    See more about :doc:`Webhooks </guide/api_webhooks>`


