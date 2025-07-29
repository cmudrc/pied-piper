import os
import piperabm as pa


# Step 4: Results
# Link: https://pied-piper.readthedocs.io/latest/step-by-step.html#step-4-results
# (Saving the measurement data)
path = os.path.dirname(os.path.realpath(__file__))
measurement = pa.Measurement(path=path)
measurement.measure()