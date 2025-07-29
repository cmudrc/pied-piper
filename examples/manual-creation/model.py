import os
import piperabm as pa


# Step 0: Create the Model
# Link: https://pied-piper.readthedocs.io/latest/step-by-step.html#step-0-create-the-model
model = pa.Model(
    path=os.path.dirname(os.path.realpath(__file__)),
    seed=10
)