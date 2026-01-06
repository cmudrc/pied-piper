Resource
========

Resources may be provided as plain dictionaries (default) or as instances of the optional :class:`piperabm.resource.Resource` helper class.
This class provides a lightweight container for resource quantities (food, water, energy) with validation and arithmetic
support. It is an optional convenience wrapper; internally, PiperABM stores
resources as plain dictionaries attached to NetworkX graph nodes.

.. code-block:: python

   from piperabm.resource import Resource

   model.society.add_agent(resources=Resource(food=1, water=2, energy=3))
   # An alternative to:
   model.society.add_agent(resources={"food":1, "water":2, "energy":3})

.. code-block:: python

   # Retrive resources as a Resource object
   resources = model.society.get_resources(id=0, object=True)
   # Retrive resources as a dictionary
   resources = model.society.get_resources(id=0)

Since the Resource class supports arithmetic operations, it can be used to easily manipulate resource quantities.

.. code-block:: python

   # Retrive resources as a Resource object
   resources = model.society.get_resources(id=0, object=True)
   resources =* 2  # Multiply all resource quantities by 2
   resources =+ Resource(food=1)  # Add 1 unit of food
   resources =- {"water": 1}  # Subtract 1 unit of water

.. autoclass:: piperabm.resource.Resource
   :members:
   :undoc-members:
   :special-members: __add__, __sub__, __mul__, __truediv__
   :show-inheritance: