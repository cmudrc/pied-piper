import matplotlib.pyplot as plt

from piperabm.path import Path
from piperabm.decision import Move
from piperabm.transportation import Foot
from piperabm.unit import Date, DT


path = Path()
path.add(pos=[200, 200])
path.add(pos=[0, 0])
path.add(pos=[0, 300])
path.add(pos=[400, 300])
path.add(pos=[0, 0])
path.add(pos=[200, 200])

start_date = Date(2020, 1, 1)

move = Move(
    start_date=start_date,
    path=path,
    transportation=Foot()
)

action_duration = move.duration().total_seconds()
video_duration = 1  # seconds
fps = 20
total_frames = video_duration * fps
step_size = action_duration / total_frames

for i in range(total_frames+1):
    delta_t = i*step_size
    time = start_date + DT(seconds=delta_t)
    position = move.pos(time)
    plt.clf()
    plt.gca().set_title('Date: ' + str(time), fontsize=10)
    #plt.gca().axis('equal')
    plt.xlim(-100, 500)
    plt.ylim(-100, 500)
    plt.scatter(*position, color='black')
    plt.pause(interval=1/fps)

plt.show()