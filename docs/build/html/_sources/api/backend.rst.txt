Backends
===============================

PiperABM stores model state directly on NetworkX graphs for interoperability and
custom analysis.

- :class:`~piperabm.infrastructure.Infrastructure` uses a NetworkX undirected graph (``Graph``)
  accessible via ``model.infrastructure.G``.
- :class:`~piperabm.society.Society` uses a NetworkX undirected multigraph (``MultiGraph``)
  accessible via ``model.society.G``.

Node and edge attributes are stored directly on these graphs. This enables
tight integration with the NetworkX ecosystem and supports bulk / vectorized
workflows. Direct graph manipulation bypasses validation performed by the
high-level API and is therefore intended for advanced users.

Example: validated API vs direct graph access
---------------------------------------------

.. code-block:: python

   # Safe, validated API
   food = model.society.get_resource(agent_id, "food")
   model.society.set_resource(agent_id, "food", value=food / 10)

.. code-block:: python

   # Advanced usage: direct graph access (bypasses validation)
   G = model.society.G
   food = G.nodes[agent_id]["food"]
   G.nodes[agent_id]["food"] = food / 10

Bulk updates (example)
----------------------

.. code-block:: python

   G = model.society.G
   for node_id, attrs in G.nodes(data=True):
       if attrs.get("type") == "agent" and attrs.get("alive", True):
           attrs["food"] *= 0.9