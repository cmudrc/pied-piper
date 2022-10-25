import matplotlib.pyplot as plt

from pied_piper.tools.path import Path
from pied_piper.decision import Move
from pied_piper.transportation import Foot
from pied_piper.tools import date


path = Path()
path.add(pos=[0, 0])
path.add(pos=[0, 300])
path.add(pos=[400, 300])

move = Move(
    start_date=date(2020, 1, 1),
    path=path,
    transportation=Foot()
)

print(move.action_duration())

#plt.plot(x_list, y_list)