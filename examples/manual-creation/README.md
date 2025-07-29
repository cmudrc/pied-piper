In this example, we demonstrate how to automatically create both infrastructure and society to run a simulation.

# Running the Example

To run the example, execute the the [`main.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/main.py) file.

# Understanding the Steps:

This example follows the steps already covered in [Step-by-Step Usage Guide](https://pied-piper.readthedocs.io/latest/step-by-step.html).

## [Step 0: Create model](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-0-create-the-model)

The [`model.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/model.py) file creates an instance of `Model` class.

## [Step 1: Build the Infrastructure](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-1-build-the-infrastructure)

The [`infrastructure.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/infrastructure.py) file imports the `Model` instance from [`model.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/model.py) file and manually adds  infrastructure elements to it one by one. If this file is executed individually, the following figure will be shown along the information about the infrastructure network elements.

![Infrastructure Creation](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/infrastructure.png?raw=true)  
*Automatically generated infrastructure grid.*

## [Step 2: Build the Society](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-2-build-the-society)

The [`society.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/society.py) file imports the `Model` instance from [`infrastructure.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/infrastructure.py) file and manually adds agents to it. If this file is executed individually, the information about the society network is shown.

## [Step 3: Run](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-3-run)

The [`run.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/run.py) file imports the `Model` instance from [`society.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/society.py) file and runs the model. Based on saving preferences, it will generate [`result`](https://github.com/cmudrc/pied-piper/tree/main/examples/manual-creation/result) folder with following files:
- [`initial.json`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/result/initial.json): This file includes the state of the model before running the simulation.
- [`simulation.json`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/result/simulation.json): This file includes the differences between steps of simulation (deltas). Whenever each step of simulation is finished, the changes compared to previous state is evaluated and saved.
- [`final.json`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/result/final.json): This file includes the state of the model after the simulation is complete.
- [`transactions.csv`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/result/transactions.csv): This file includes the transaction between agents. 

## [Step 4: Results](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-4-results)

The [`animate.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/animate.py) file creates an instance of `Model` class and load the saved simulation results. Then, by running `animate` method,  This will render the [`animation.mp4`](https://github.com/cmudrc/pied-piper/blob/main/examples/manual-creation/result/animation.mp4) in the [`result`](https://github.com/cmudrc/pied-piper/tree/main/examples/manual-creation/result) folder. This is useful for face-validation of the results.