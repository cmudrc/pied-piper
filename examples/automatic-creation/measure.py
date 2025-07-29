import os
import piperabm as pa


# Step 4: Results
# Link: 
path = os.path.dirname(os.path.realpath(__file__))
measurement = pa.Measurement(path=path)
measurement.measure()