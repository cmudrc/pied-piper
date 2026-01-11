.. PiperABM documentation master file, created by
   sphinx-quickstart on Mon Jul 14 18:59:44 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   Add your content using ``reStructuredText`` syntax. See the
   `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
   documentation for details.

PiperABM Documentation
======================

This is the documentation for PiperABM, a Python-based agent-based modeling framework designed for simulating community resilience.

.. figure:: https://raw.githubusercontent.com/cmudrc/pied-piper/refs/heads/main/assets/960px-Pied_Piper2.jpg
   :align: center
   :alt: Illustration of the Pied Piper of Hamelin
   :class: main-figure
   
   Illustration by Kate Greenaway, originally published in Robert Browning’s *The Pied Piper of Hamelin*.

Getting Started
---------------

- Start with :doc:`usage/installation`
- Follow the :doc:`usage/step-by-step` tutorial
- Explore practical examples in the
  `examples directory <https://github.com/cmudrc/pied-piper/tree/main/examples>`_

Project Links
-------------

- **Source code (GitHub):** https://github.com/cmudrc/pied-piper
- **Python package (PyPI):** https://pypi.org/project/piperabm/
- **JOSS paper:** https://joss.theoj.org/papers/482e67b36285c6a9e5c00b15cc26607f

If you use PiperABM in academic work, please cite the accompanying JOSS paper (currently under review).


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Usage Guide

   usage/installation
   usage/step-by-step
   usage/satellite
   usage/backend

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: API Reference
      
   api/model
   api/measurement
   api/infrastructure
   api/society
   api/resource
   api/projection
   api/mesh

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Contributing

   contributing/contributing
