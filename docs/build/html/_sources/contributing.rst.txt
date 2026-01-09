Contributing
============

We welcome contributions to PiperABM, including small bug fixes, documentation improvements, and extensions to existing model components. The project is structured to make targeted, modular contributions straightforward.

Repository structure
--------------------

The core source code lives in the ``piperabm/`` directory and is organized by domain:

- ``piperabm/economy/``
- ``piperabm/infrastructure/``
- ``piperabm/model/``
- ``piperabm/society/``
- ``piperabm/tools/``

Each submodule is designed to be as self-contained as possible, allowing contributors to modify or extend a single component without affecting the rest of the codebase.

Where to make changes
---------------------

Common contribution tasks map to the following locations:

- **Fix or improve documentation text**  
  Edit the corresponding ``.rst`` files in ``docs/source/``.

- **Improve or extend API documentation**  
  Edit or add docstrings directly in the relevant files under ``piperabm/``.  
  API documentation is automatically generated from in-code docstrings using Sphinx.

- **Modify or add core functionality**  
  Make changes in the appropriate submodule under ``piperabm/`` and add or update the corresponding unit tests.

- **Add examples or tutorials**  
  Place new examples in the ``examples/`` directory or add tutorial-style documentation under ``docs/source/``.

Testing
-------

PiperABM uses automated unit tests to ensure correctness and maintainability.

- **Run the full test suite** from the project root:

  .. code-block:: bash

     python tests.py

- **Test organization**

  Tests are organized to mirror the source structure:

  - ``piperabm/<module>/`` → ``tests/test_<module>/``

  Each test file can be run independently to test its corresponding module in isolation.

When adding new features or modifying existing behavior, contributors are encouraged to include appropriate unit tests.

Examples and tutorials
----------------------

The ``examples/`` directory contains runnable, self-contained examples that demonstrate different modeling workflows and extension patterns in PiperABM.

A curated overview of all available examples, along with brief descriptions and links, is provided in:

- ``examples/README.md``

Examples cover a range of use cases, including minimal single-agent setups, multi-agent interactions, automatic and manual model creation, customization of decision-making and degradation behavior, satellite-based maps, and parallel execution of multiple scenarios.

Each example directory typically contains Python scripts defining the model, infrastructure, and society, along with a local ``README.md`` explaining how to run the example and what it demonstrates.

Contributors adding new examples are encouraged to:
- Place them in a new or existing subdirectory under ``examples/``
- Keep examples self-contained and runnable
- Add an entry to ``examples/README.md`` describing the new example
- Include a short ``README.md`` explaining the purpose and usage of the example

Building the documentation locally
----------------------------------

PiperABM documentation is built using the Sphinx engine. API documentation is generated automatically from in-code docstrings, while conceptual guides and tutorials are maintained as standalone ``.rst`` files in ``docs/source/``.

To build the documentation locally:

1. Install the documentation dependencies:

   .. code-block:: bash

      pip install -r docs/requirements.txt

2. From the ``docs/`` directory, build the HTML documentation:

   .. code-block:: bash

      make html

   On Windows, use:

   .. code-block:: bash

      make.bat html

3. Open the generated documentation in a browser:

   .. code-block:: bash

      docs/build/html/index.html

This allows contributors to verify documentation formatting, API references, and tutorial content before submitting changes.

Development workflow
--------------------

A typical contribution workflow is:

1. Identify the relevant module or documentation file.
2. Make a focused change.
3. Run the test suite using ``python tests.py``.
4. Build the documentation locally if documentation or docstrings were modified.
5. Submit a pull request describing the change.

New features should include docstrings and, where appropriate, unit tests to ensure they are included in the documentation and test coverage.

Versioning and releases
-----------------------

When preparing a new release, please ensure that the project version number is updated consistently across the codebase and documentation.

The following files must be updated to match the new version:

- ``piperabm/__init__.py``  
  Update the ``__version__`` variable:

  .. code-block:: python

     __version__ = "0.1.2"

- ``pyproject.toml``  
  Update the project version:

  .. code-block:: toml

     version = "0.1.2"

- ``docs/source/conf.py``  
  Update the documentation release string:

  .. code-block:: python

     release = "0.1.2"

Keeping these values in sync ensures that the installed package, published metadata, and generated documentation all report the same version number.