import matplotlib.pyplot as plt

from piperabm.environment import Environment
from piperabm.agents import Society
from piperabm.unit import DT, Date


class Model:

    def __init__(
        self,
        environment: Environment,
        society: Society,
        step_size=None,
        current_step=0,
        current_date=Date.today()
    ):
        self.env = environment
        self.society = society
        self.add_step_size(step_size)
        self.current_step = current_step
        self.current_date = current_date

    def add_step_size(self, step_size):
        """
        Check if the step_size is in DT format, or else convert it to DT
        """
        if isinstance(step_size, DT):
            self.step_size = step_size
        elif isinstance(step_size, (float, int)):
            self.step_size = DT(seconds=step_size)
        else:
            raise ValueError

    def burnout(self):
        """
        Buroun phase for initiation of model
        """
        start_date = self.env.find_oldest_element()
        end_date = self.current_date
        self.env.update_elements(start_date, end_date)

    def run_step(self):
        if self.current_step == 0:
            self.burnout()
        start_date = self.current_date
        end_date = start_date + self.step_size
        self.env.update_elements(start_date, end_date)
        self.society.update_elements(start_date, end_date)

        path = self.env.to_path(start_date, end_date)
        #path.show()
        ####
        self.current_date = end_date
        self.current_step += 1
        
        #print(self.current_step, self.current_date)

    def run(self, n=1, show=True):
        """
        Run model for n steps further
        """
        for i in range(n):
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
    def to_plt(self, ax=None):
        """
        Add elements to plt
        """
        if ax is None:
            ax = plt.gca()
        start_date = self.current_date - self.step_size
        end_date = self.current_date
        args = (ax, start_date, end_date)
        self.env.to_plt(*args)
        self.society.to_plt(ax)
    
    def show(self):
        self.to_plt()
        plt.gca().set_title(self.current_date)
        plt.show()
