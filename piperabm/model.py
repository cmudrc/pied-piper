import matplotlib.pyplot as plt

from piperabm.environment import Environment
from piperabm.unit import Unit, DT
from piperabm.graphics.plt import agent_to_plt


class Model:

    def __init__(
        self,
        environment: Environment,
        agents=[],
        step_size=None,
        current_step=0,
        current_date=None
    ):
        self.add_step_size(step_size)
        self.current_step = current_step
        self.current_date = current_date

        self.environment = environment
        self.agents = agents

    def add_step_size(self, step_size):
        if isinstance(step_size, DT):
            self.step_size = step_size
        elif isinstance(step_size, (float, int)):
            self.step_size = DT(seconds=step_size)

    def update_environment(self, next_date):
        """
        Check activeness of all elements in the environment until the next_date
        """
        if self.current_date < next_date:
            if self.current_step == 0:
                start_date = self.environment.find_oldest_element(self.environment.settlements)
                if start_date is None: start_date = self.current_date
            else:
                start_date = self.current_date
            end_date = next_date
            self.environment.update_elements(start_date, end_date)
        else:
            raise ValueError

    def update_agents(self, next_date):
        # Prepare:
        for agent in self.agents:
            if agent.asset is not None and agent.active:
                agent.asset.refill(next_date - self.current_date)
        # Phase I: Internal
        for agent in self.agents:
            if agent.asset is not None and agent.active:
                agent.solve()
        # Phase II: Within Settlement
        # Phase III: Explore and Exploit
        # Finalize:
        for agent in self.agents:
            agent.finalize()

    def run_step(self):
        next_date = self.step_size + self.current_date
        #print(self.current_date, next_date)
        self.update_environment(next_date)
        self.update_agents(next_date)
        self.current_step += 1

    def run(self, steps=1):
        for i in range(steps):
            self.run_step()

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        self.environment.to_plt(ax)
        for agent in self.agents:
            agent_to_plt(agent.to_dict(), ax)

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')
        plt.xlim(self.environment.x_lim)
        plt.ylim(self.environment.y_lim)
        self.to_plt(ax)
        plt.show()


if __name__ == "__main__":
    from piperabm import Agent, Settlement, Environment, Model
    from piperabm.asset import Asset, Resource, Produce, Use, Storage, Deficiency
    from piperabm.unit import Unit, Date


    agents = [
        Agent(
            name='John',
            pos=[1, 1],
            settlement='home_1'
        ),
        Agent(
            name='Betty',
            pos=[0.5, 0.5]
        )
    ]
    settlements = [
        Settlement(
            name='home_1',
            pos=[0, 0],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 50
            },
            initiation_date=Date(2000, 1, 1),
            distribution={
                'type': 'dirac delta',
                'main': Unit(5, 'day').to_SI(),
            },
            seed=None
        ),
        Settlement(
            name='home_2',
            pos=[100, 100],
            max_population=10,
            initiation_date=Date(1999, 12, 29),
        ),
        Settlement(
            name='home_3',
            pos=[200, -100],
            max_population=10,
            boundery={
                'type': 'rectangular',
                'height': 100,
                'width': 200,
                'theta': 0.3
            },
            initiation_date=Date(1999, 12, 29),
        ),
    ]
    links = []
    asset = Asset()
    '''
    links = [
        Road(
            start_node='home_1',
            end_node='home_2',
            double_sided=True,
            name='sample road',
            initiation_date=date(2000, 1, 1),
            distribution={
                'type': 'dirac delta',
                'main': Unit(10, 'day'),
            },
            seed=None
        )
    ]
    '''
    
    env = Environment(
        x_lim=[-300, 450],
        y_lim=[-250, 250],
        asset=asset,
        settlements=settlements,
        links=links
    )

    m = Model(
        environment=env,
        agents=agents,
        step_size=Unit(5, 'day').to_SI(),
        current_step=0,
        current_date=Date(2000, 1, 1),
    )
    #m.to_graph()
    #m.environment.show()
    #print(m.environment.settlements[0].active)
    m.run_step()
    m.show()
    #print(m.environment.settlements[0].active)
    #print(m.current_infrastructures)
