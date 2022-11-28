from piperabm import Settlement, Environment
from piperabm.boundery import Circular, Rectangular


s_1 = Settlement(
    name='home_1',
    pos=[-50, 50],
)
s_2 = Settlement(
    name='home_2',
    pos=[50, 40],
    boundery=Circular(radius=30)
)
s_3 = Settlement(
    name='home_3',
    pos=[0, -30],
    boundery=Rectangular(width=70, height=40, theta=0.3)
)

env = Environment(
    x_lim=[-150,150],
    y_lim=[-100,100],
    settlements=[s_1, s_2, s_3]
)
env.show()
