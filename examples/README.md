# Examples

Examples are designed to show how different capabilities of PiperABM, how it behaves and most imprtantly, how to transalte real-world scenarios into the simulation setup.

## [Single Agent](https://github.com/cmudrc/pied-piper/tree/main/examples/single-agent)

This is one of the most simple setups.
The world has only one market and one home with one agent living there.
The agent starts moving to the market.
The result is animated.

## [Two Agent at Home](https://github.com/cmudrc/pied-piper/tree/main/examples/two-agents-at-home)

This is one the most simple setups. The world contains only one home with two agents living there as family.
They start with different amount of resources and thus, they eventually share it with each other when the simulation runs.

## [Automatic Creation](https://github.com/cmudrc/pied-piper/tree/main/examples/automatic-creation)

In this example, we demonstrate how to automatically generate both infrastructure and society to run a simulation.

## [Manual Creation](https://github.com/cmudrc/pied-piper/tree/main/examples/manual-creation)

In this example, we demonstrate how to manually create both infrastructure and society to run a simulation.

## [Satellite Map](https://github.com/cmudrc/pied-piper/tree/main/examples/satellite-map)

This example shows how to work with satellite data and maps to create model.

## [Custom Degradation](https://github.com/cmudrc/pied-piper/tree/main/examples/custom-degradation)

In this example, we see how the user can customize degradation behavior of the infrastrcture elements of the model by providing their own `degradation.py` file.

## [Custom Decision-Making](https://github.com/cmudrc/pied-piper/tree/main/examples/custom-decision-making)

In this example, we see how the user can customize decision-making behavior of the agents in the model by providing their own `decision_making.py` file.

## [Parallel Processing](https://github.com/cmudrc/pied-piper/tree/main/examples/parallel-processing)

When working with multiple scenarios, meaning dealing with multiple instances of the `Model` class, it is a good practice to run them in parallel.
This speeds up the progress significantly.
