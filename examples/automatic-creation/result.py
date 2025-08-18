import os
import piperabm as pa


# Step 4: Results
# (Loading the measurement data)
# Link: https://pied-piper.readthedocs.io/latest/step-by-step.html#step-4-results
path = os.path.dirname(os.path.realpath(__file__))
measurement = pa.Measurement(path=path)
measurement.load()
measurement.accessibility.show()
measurement.travel_distance.show()
