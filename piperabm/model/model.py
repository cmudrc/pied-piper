import numpy as np

from piperabm.society import Society
from piperabm.environment import Environment
from piperabm.unit import DT, Date
from piperabm.log import Log
from piperabm.measure import Measures



class Model:

    def __init__(
        self,
        society: Society = None,
        environment: Environment = None,
        step_size: int = None,
        current_step: int = 0,
        current_date: Date = None,
        seed=None,
        seed_state=None
    ):
        #super().__init__()
        self.add_environment_society(environment, society)

        self.add_step_size(step_size)

        if current_step >= 0:
            self.current_step = current_step
        else:
            raise ValueError

        if current_date is None:
            self.current_date = Date.today()
        else:
            self.current_date = current_date

        self.measures = Measures()
        self.log = Log(prefix='MODEL', indentation_depth=0)
        
        if seed is not None:
            self.seed = seed
            np.random.default_rng(self.seed)
            if seed_state is not None:
                np.random.set_state(seed_state)

    def add_environment_society(
            self,
            environment: Environment,
            society: Society
        ):
        """
        Add environment and society to the model and create their entanglement
        """    
        self.environment = environment
        self.society = society
        if society is not None and environment is not None:
            ''' create mutual entanglement '''
            self.environment.society = self.society
            self.society.environment = self.environment

    def get_random_state(self):
        return np.random.get_state()

    def add_step_size(self, step_size):
        """
        Check if the step_size is in DT format, or else convert it to DT
        """
        if step_size is None:
            self.step_size = DT(days=1)
        elif isinstance(step_size, DT):
            self.step_size = step_size
        elif isinstance(step_size, (float, int)):
            self.step_size = DT(seconds=step_size)
        else:
            raise ValueError

    def burnout(self):
        """
        Burnout phase for initiating the model
        """
        start_date = self.environment.oldest_date()
        end_date = self.current_date
        #''' log '''
        #msg = self.log.message__burnout(start_date, end_date)
        #print(msg)
        self.environment.update(start_date, end_date)

    def run_step(self):
        """
        Run a single step
        """
        #print(self.current_step, self.current_date)
        if self.current_step == 0:
            self.log.reset()
            self.burnout()
        start_date = self.current_date
        end_date = start_date + self.step_size
        #''' log '''
        #msg = self.log.message__date_step(start_date, end_date, self.current_step)
        #print(msg)
        self.environment.update(start_date, end_date)
        self.society.update(start_date, end_date)
        self.measures.read_data(self.society, start_date, end_date)
        self.current_date = end_date
        self.current_step += 1

    def run(self, n=1, log=True):
        """
        Run model for n steps further
        """
        for _ in range(n):
            self.run_step()
            '''
            plt.clf()
            plt.gca().set_title(self.current_date)
            self.env.to_plt()
            plt.pause(interval=0.1)
            #plt.xlim(m.environment.x_lim)
            #plt.ylim(m.environment.y_lim)
        plt.show()
        '''

