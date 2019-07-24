=================
Essais
=================

Only 
======

.. only:: latex

   This appears only in LaTeX output.

.. only:: html

   This appears only in HTML output. 



Raw HTML
=========


Raw HTML and object tag: 

.. raw:: html

    <object data="/_images/user_guide/platform/button-add-file.svg" type="image/svg+xml"></object>


Raw HTML and file option:

.. raw:: html
    :file: /_images/user_guide/platform/button-add-file.*



Directive image
================

image : 

.. image:: /_images/user_guide/platform/button-add-file.svg

Only HTML
-------------

.. only:: html
    .. image:: /_images/user_guide/platform/button-add-file.svg


Only LaTeX
-------------

.. only:: latex
    .. image:: /_images/user_guide/platform/button-add-file.png


Directive with wildcard
------------------------

.. image:: /_images/user_guide/platform/button-add-file.*


Include 
==========

Inclusion of a file

.. include:: /_images/user_guide/platform/button-add-file.svg


.. include:: /_images/user_guide/platform/button-add-file.svg
   :literal: