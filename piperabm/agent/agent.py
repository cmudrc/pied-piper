from copy import deepcopy

#from piperabm.agent.brain import Brain
from piperabm.object import PureObject
from piperabm.resources import Resources
from piperabm.time import DeltaTime, Date
from piperabm.transporation import Transportation
from piperabm.actions.queue import Queue
from piperabm.agent.config import *


class Agent(PureObject):

    def __init__(
        self,
        index = None,
        society = None,
        name: str = "",
        home_index: int = None,
        alive: bool = True,
        transportation: Transportation = None,
        resources: Resources = None,
        fuels_rate_idle: Resources = None,
        balance: float = 0,
        income: float = 0,
        socioeconomic_status: float = 1,
    ):
        super().__init__()
        """ binding """
        self.index = index
        self.society = society

        """ decision making """
        #self.brain = Brain()
        self.brain = None

        """ identity """
        self.name = name
        self.alive = alive
        self.death_reason = None
        self.home_index = home_index
        self.socioeconomic_status = socioeconomic_status
        self.type = "agent"

        """ transporation """
        if transportation is None: transportation = WALK
        self.transportation = transportation

        """ queue """
        self.queue = Queue()

        """ resource """
        if resources is None:
            resources = deepcopy(RESOURCES_DEFAULT)
        self.resources = resources

        if fuels_rate_idle is None:
            fuels_rate_idle = deepcopy(FUELS_RATE_HUMAN_IDLE)
        self.fuels_rate_idle = fuels_rate_idle

        if income < 0: raise ValueError
        self.income = income

        if balance < 0: raise ValueError
        self.balance = balance

    def check_liveness(self) -> bool:
        """
        Check whether agent is alive
        """
        if self.alive is True:
            resources_zero = self.resources.check_empty(RESOURCES_VITAL)
            if len(resources_zero) > 0:  # died
                self.alive = False
                self.death_reason = resources_zero[0]  # one reason is enough
        return self.alive
    
    @property
    def source(self):
        return self.resources.source
    
    @property
    def demand(self):
        return self.resources.demand

    def update(self, date_start: Date = Date.today(), date_end: Date = Date.today()) -> None:
        """
        Reduce the idle_fuel_consumption from agent"s resource
        """
        if self.alive is True:
            duration = date_end - date_start
            other_rates = [] ###### from action in queue
            self.balance += self.income * duration.total_seconds()
            self.consume_resources(duration, other_rates)
            self.check_liveness()

        """ decide """
        #if self.alive is True:  
        #    self.brain.observe(self.index, self.environment, self.society)
        #    actions = self.brain.decide()
        #    self.queue.add(actions)

    def consume_resources(self, duration, other_rates: list = []):
        """
        Create ResourceDelta object based on duration and fuel_rate
        """
        if isinstance(duration, DeltaTime):
            duration = duration.total_seconds()
        total_consumption = deepcopy(self.fuels_rate_idle)
        for other_rate in other_rates:
            total_consumption.add(other_rate)
        total_consumption.mul(duration)
        remainder = self.resources.sub(total_consumption)
        return remainder

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "alive": self.alive,
            "death_reason": self.death_reason,
            "home_index": self.home_index,
            "transportation": self.transportation.serialize(),
            "queue": self.queue.serialize(),
            "resources": self.resources.serialize(),
            "fuels_rate_idle": self.fuels_rate_idle.serialize(),
            "balance": self.balance,
            "income": self.income,
            "type": self.type
        }

    def deserialize(self, dictionary: dict) -> None:
        self.name = dictionary["name"]
        self.alive = dictionary["alive"]
        self.death_reason = dictionary["death_reason"]
        self.home_index = dictionary["home_index"]
        self.transportation = Transportation()
        self.transportation.deserialize(dictionary["transportation"])
        self.queue = Queue()
        self.queue.deserialize(dictionary["queue"])
        self.resources = Resources()
        self.resources.deserialize(dictionary["resource"])
        self.fuels_rate_idle = Resources()
        self.fuels_rate_idle.deserialize(dictionary["fuels_rate_idle"])
        self.balance = dictionary["balance"]
        self.income = dictionary["income"]
        self.type = dictionary["type"]


if __name__ == "__main__":
    from piperabm.resources.samples import resources_0

    agent = Agent(
        name="John",
        resources=resources_0
    )
    agent.update()
    agent.print
