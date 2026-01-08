# Custom Decision-Making

In this example, we see how the user can customize decision-making behavior of the agents in the model by providing their own decision-making class which is inside the `decision_making.py` file.

```python
from decision_making import CustomDecisionMaking

...
model.society.set_decision_making(CustomDecisionMaking)
```
