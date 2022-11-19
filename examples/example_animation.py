import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

output = plt.plot([])
plt.close() # do not draw anything
print(output[0])

fig = plt.figure()

lines = plt.plot([])
line = lines[0]
# the same as:
#line, = plt.plot([])

# other setup


# frame value starts from 0 until total_frames
def animate(frame):
    # update plot
    pass
#anim = FuncAnimation(fig, )
