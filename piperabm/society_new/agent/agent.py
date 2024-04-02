from piperabm.object import PureObject
from piperabm.matter_new import Matter
from piperabm.time import DeltaTime
from piperabm.transportation import Transportation
from piperabm.transportation.samples import transportation_0 as walk
from piperabm.actions import ActionQueue
from piperabm.society_new.agent.brain import Brain


class Agent(PureObject):

    section = 'society'
    category = 'node'
    type = 'agent'

    def __init__(
        self,
        name: str = '',
        transportation: Transportation = walk,
        fuels_rate_idle: Matter = Matter({'food': 1, 'water': 1, 'energy': 1}),
        socioeconomic_status: float = 1,
        balance: float = 1,
        resources: Matter = Matter({'food': 1, 'water': 1, 'energy': 1}),
        enough_resources: Matter = Matter({'food': 1, 'water': 1, 'energy': 1}),
        max_time_outside: DeltaTime = DeltaTime(hours=1),
    ):
        super().__init__()
        self.society = None # Binding

        # Identity
        self.name = name
        self.id = None
        self.transportation = transportation
        self.socioeconomic_status = socioeconomic_status
        
        # Location
        self.pos = None
        self.home = None
        self.current_node = None
        self.time_outside = DeltaTime(seconds=0)
        self.max_time_outside = max_time_outside
        
        # Actions
        self.brain = Brain(agent=self)
        self.queue = ActionQueue()
        self.queue.agent = self  # Binding

        # Resources
        self.fuels_rate_idle = fuels_rate_idle
        self.resources = resources
        self.enough_resources = enough_resources
        self.balance = balance
        self.alive = True
        self.vital_resources = ['food', 'water']
        self.death_reasons = None

    def check_alive(self) -> bool:
        """
        Check whether agent is alive
        """
        if self.alive is True:
            resources_zero = self.resources.check_empty(self.vital_resources)
            if len(resources_zero) > 0:  # Died
                self.alive = False
                self.death_reasons = resources_zero
        return self.alive

    def is_home(self) -> bool:
        """
        Check whether agent is in home
        """
        result = None
        if self.home is None:
            print('home id is not defined.')
            raise ValueError
        else:
            if self.current_node == self.home:
                result = True
            else:
                result = False
        return result
    
    @property
    def accessibility(self):
        ratios = self.resources / self.enough_resources
        ratios = ratios.library
        for name in ratios:
            ratio = ratios[name]
            if ratio > 1:
                ratios[name] = 1
        return ratios
    
    '''
    def utility(self, resource_name):
        return self.resources(name=resource_name)
    '''

    def update(self, duration: DeltaTime) -> None:
        """
        Update agent
        """
        """ Check being alive """
        self.check_alive()
        """ Update assets """
        if self.alive is True:
            """ Income """
            self.balance += self.income * duration.total_seconds()
            """ Consume resources """
            fuels = self.fuels_rate_idle * duration.total_seconds()
            self.resources - fuels
            self.queue.update(duration)
            """ How long it has been out of home? """
            if self.is_home():
                self.time_outside = DeltaTime(seconds=0)
            else:
                self.time_outside += duration
        """ Decide """
        if self.alive is True:
            self.brain.decide()

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['name'] = self.name
        dictionary['id'] = self.id
        dictionary['transportation'] = self.transportation.serialize()
        dictionary['socioeconomic_status'] = self.socioeconomic_status
        dictionary['pos'] = self.pos
        dictionary['home'] = self.home
        dictionary['current_node'] = self.current_node
        dictionary['time_outside'] = self.time_outside.total_seconds()
        dictionary['max_time_outside'] = self.max_time_outside.total_seconds()
        dictionary['queue'] = self.queue.serialize()
        dictionary['fuels_rate_idle'] = self.fuels_rate_idle.library
        dictionary['resources'] = self.resources.library
        dictionary['enough_resources'] = self.enough_resources.library
        dictionary['balance'] = self.balance
        dictionary['alive'] = self.alive
        dictionary['vital_resources'] = self.vital_resources
        dictionary['death_reasons'] = self.death_reasons
        dictionary['type'] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.id = dictionary['id']
        self.transportation = Transportation()
        self.transportation.deserialize(dictionary['transportation'])
        self.socioeconomic_status = dictionary['socioeconomic_status']
        self.pos = dictionary['pos']
        self.home = dictionary['home']
        self.current_node = dictionary['current_node']
        self.time_outside = DeltaTime(seconds=dictionary['time_outside'])
        self.max_time_outside = DeltaTime(seconds=dictionary['max_time_outside'])
        self.queue = ActionQueue()
        self.queue.deserialize(dictionary['queue'])
        self.queue.agent = self
        self.fuels_rate_idle = Matter(dictionary['fuels_rate_idle'])
        self.resources = Matter(dictionary['resources'])
        self.enough_resources = Matter(dictionary['enough_resources'])
        self.balance = dictionary['balance']
        self.alive = dictionary['alive']
        self.vital_resources = dictionary['vital_resources']
        self.death_reasons = dictionary['death_reasons']


if __name__ == '__main__':
    agent = Agent()
    print(agent)
