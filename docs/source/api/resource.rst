Resource
========

The :class:`piperabm.resource.Resource` class provides a lightweight container
for resource quantities (food, water, energy) with validation and arithmetic
support. It is an optional convenience wrapper; internally, PiperABM stores
resources as plain dictionaries attached to NetworkX graph nodes.

.. autoclass:: piperabm.resource.Resource
   :members:
   :undoc-members:
   :special-members: __add__, __sub__, __mul__, __truediv__
   :show-inheritance: