from piperabm.environment import Environment
from piperabm.society import Society
from piperabm.time import DeltaTime


class Model:

    def __init__(
        self,
        environment: Environment = None,
        society = None,
        step_size = None,
    ):
        self.add_environment(environment)
        self.add_society(society)

        if isinstance(step_size, (float, int)):
            step_size = DeltaTime(seconds=step_size)
        if isinstance(step_size, DeltaTime):
            self.step_size = step_size
        else:
            raise ValueError

    def add_environment(self, environment: Environment = None):
        if environment is None:
            environment = Environment(proximity_radius=1)
        self.environment = environment
        if self.society is not None:
            self.environment.society = self.society
        
    def add_society(self, society: Society = None):
        if society is None:
            society = Society()
        self.society = society
        if self.environment is not None:
            self.society.environment = self.environment


if __name__ == "__main__":
    from piperabm.environment.samples import environment_2 as environment
    model = Model(
        environment=environment,
        society=None,
        step_size=1
    )

    
        