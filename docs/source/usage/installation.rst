.. _installation:

Installation
================================
Install the package using pip:

.. code-block:: bash

    pip install piperabm

Python version requirements
---------------------------

PiperABM is tested and officially supported on **Python 3.10 through 3.13**.

While the package may work on older Python versions with compatible dependencies,
these environments are not tested and are not officially supported.

Optional dependencies
---------------------

Animation support in PiperABM relies on the external tool **ffmpeg**.

If you plan to use ``model.animate()`` to save animations to video files, you must have ``ffmpeg`` installed and available on your system PATH.

Installation instructions for ffmpeg are platform-specific and can be found at:

https://ffmpeg.org/download.html

Quick install examples:

- macOS (Homebrew): ``brew install ffmpeg``
- Ubuntu/Debian: ``sudo apt install ffmpeg``
- Conda: ``conda install -c conda-forge ffmpeg``

If ffmpeg is not installed, animation features will be unavailable, but all other
PiperABM functionality will work normally.