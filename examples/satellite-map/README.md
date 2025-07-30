In this example, we demonstrate how to work with satellite data and maps to create model.

# Running the Example

To run this example, execute the [`main.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/run.py) file.

# Understanding the Steps:

This example follows the steps already covered in [Working with Satellite Data](https://pied-piper.readthedocs.io/latest/satellite.html).

![Map](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/parker,pa-points.png?raw=true)  
*Map of the Parker, PA.*

## Points Coordinates

The [`points.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/points.py) file contains latitude and longitude of the points that are labeled in the figure below:

![Labeled Points on the Map](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/parker,pa-points.png?raw=true)  
*Points of labeled on the map*

These points are used for both loading the streets and meshing the residential areas to randomly generate home nodes.

## Streets

The [`streets.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/streets.py) file contains a list of lists. Each element of this list is the label of points that create one street.

## Mesh

The [`mesh.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/mesh.py) file contains a list of triangles that cover the residential areas of the city with meshes. Each triangle has a corresponding density. For example, the triangle 6 has a lower density of homes so the density value for this triangle is lower than the rest.

![Meshed Residential Areas](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/parker,pa-mesh.png?raw=true)  
*Meshes covering the residential areas on the map*

## 



The [`society.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/society.py) file imports the `Model` instance from [`infrastructure.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/infrastructure.py) file and adds an automatically generated society to it. If this file is executed individually, the information about the society network is shown.

## [Step 3: Run](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-3-run)

The [`run.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/run.py) file imports the `Model` instance from [`society.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/society.py) file and runs the model. Based on saving preferences, it will generate [`result`](https://github.com/cmudrc/pied-piper/tree/main/examples/automatic-creation/result) folder with following files:
- [`initial.json`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/initial.json): This file includes the state of the model before running the simulation.
- [`simulation.json`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/simulation.json): This file includes the differences between steps of simulation (deltas). Whenever each step of simulation is finished, the changes compared to previous state is evaluated and saved.
- [`final.json`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/final.json): This file includes the state of the model after the simulation is complete.
- [`transactions.csv`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/transactions.csv): This file includes the transaction between agents. 

## [Step 4: Results](https://pied-piper.readthedocs.io/latest/step-by-step.html#step-4-results)

The [`measure.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/measure.py) file creates an instance of `Measurement` class and do the measurements using the saved files. This will result in [`measurement.json`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/measurement.json) in the [`result`](https://github.com/cmudrc/pied-piper/tree/main/examples/automatic-creation/result) folder that can be used for loading the meareuments later.
Finaly, [`result.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result.py) file loades the measurements and visualizes them as follows:

![Accessibility](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/accessibility.png?raw=true)  
*Agents resource accessibility scores over time*

![Travel Distance](https://github.com/cmudrc/pied-piper/blob/main/examples/automatic-creation/result/travel_distance.png?raw=true)  
*Total travel distances of agents vs. time*