import matplotlib.pyplot as plt


from piperabm import Settlement, Link, Environment, Model
from piperabm.boundery import Circular, Rectangular
from piperabm.degradation import DiracDelta, Gaussian
from piperabm.unit import Date, Unit


s_0 = Settlement(
    name='home_0',
    pos=[-50, 50],
)
s_1 = Settlement(
    name='home_1',
    pos=[50, 40],
    boundery=Circular(radius=30),
    initiation_date=Date(2020,1,1),
    distribution=DiracDelta(
        main=Unit(5,'day').to_SI()
    )
)
s_2 = Settlement(
    name='home_2',
    pos=[0, -30],
    boundery=Rectangular(width=70, height=40, theta=0.3),
    initiation_date=Date(2020,1,1),
    distribution=Gaussian(
        mean=Unit(10,'day').to_SI(),
        sigma=Unit(1,'day').to_SI()
    ),
    seed=None
)

env = Environment(
    x_lim=[-150,150],
    y_lim=[-100,100],
    settlements=[s_0, s_1, s_2],
    links=[]
)

m = Model(
    environment=env,
    step_size=Unit(1, 'day').to_SI(),
    current_date=Date(2020,1,1)
)

i = 1
while 20 > i:
    plt.clf()
    plt.gca().set_title("days passed: " + str(i))
    plt.xlim(m.environment.x_lim)
    plt.ylim(m.environment.y_lim)
    m.run()
    m.to_plt()
    plt.pause(interval=0.1)
    i += 1

plt.show()
