import os
import piperabm as pa


# Step 4: Results
# (Animate the result)
# Link: https://pied-piper.readthedocs.io/latest/step-by-step.html#step-4-results
model = pa.Model(path=os.path.dirname(os.path.realpath(__file__)))  # Load the model
model.animate()
