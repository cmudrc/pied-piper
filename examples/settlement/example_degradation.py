import matplotlib.pyplot as plt

from piperabm import Settlement, Agent
from piperabm import Model
from piperabm.unit import Date, DT

'''
s_1 = Settlement(
    name='s_1',
    pos=[0, 0],
    boundery={
        'type': 'circular',
        'radius': 10,
    },
    active=True,
    initiation_date=date(2000, 1, 1),
    distribution={
        'type': 'dirac delta',
        'main': dt(days=5)
    }
)'''

all_agents = [
    Agent(
        name='John',
        pos=[1, 1]
    ),
    Agent(
        name='Betty',
        pos=[1, 1]
    )
]

s = Settlement(
    name='s_2',
    pos=[50, 50],
    boundery={
        'type': 'rectangular',
        'width': 20,
        'height': 10,
        'theta': 0.3
    },
    active=True,
    initiation_date=Date(2000, 1, 1),
    distribution={
        'type': 'dirac delta',
        'main': DT(days=5)
    }
)

from piperabm.graphics.plt.settlement import settlement_to_plt

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim([25, 75])
plt.ylim([25, 75])

settlement_to_plt(s.to_dict())

plt.show()
