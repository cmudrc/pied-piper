In this example, we demonstrate how to automatically create both infrastructure and society to run a simulation. It follows the steps already covered in [Step-by-Step Usage Guide](https://pied-piper.readthedocs.io/latest/step-by-step.html).

## [Step 0: Create model](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-0-create-the-model)

The `model.py` file creates an instance of `Model` class.

## [Step 1: Build the Infrastructure](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-1-build-the-infrastructure)

The [`infrastructure.py`]() file imports the `Model` instance from [`model.py`]() file and adds an automatically generated infrastructure to it. If this file is executed individually, the following figure will be shown along the information about the infrastructure network elements.

![Infrastructure Creation](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/infrastructure.png?raw=true)  
*Automatically generated infrastructure grid.*

## [Step 2: Build the Society](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-2-build-the-society)

The [`society.py`]() file imports the `Model` instance from [`infrastructure.py`]() file and adds an automatically generated society to it. If this file is executed individually, the following figure will be shown.

## [Step 3: Run](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-3-run)

The [`run.py`]() file imports the `Model` instance from [`society.py`]() file and runs the model. Based on saving preferences, it will generate [`result`]() folder with following files:
- [`initial.json`](): This file includes the state of the model before running the simulation.
- [`simulation.json`](): This file includes the differences between steps of simulation (deltas). Whenever each step of simulation is finished, the changes compared to previous state is evaluated and saved.
- [`final.json`](): This file includes the state of the model after the simulation is complete.
- [`transactions.csv`](): This file includes the transaction between agents. 

## [Step 4: Results](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-4-results)

The [`measure.py`]() file creates an instance of `Measurement` class and do the measurements using the saved files. This will result in [`measurement.json`]() in the [`result`]() folder that can be used for loading the meareuments later.
Finaly, [`result.py`]() file loades the measurements and visualizes them as follows:

![Accessibility](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/accessibility.png?raw=true)  
*Agents resource accessibility scores over time*

![Travel Distance](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/travel_distance.png?raw=true)  
*Total travel distances of agents vs. time*