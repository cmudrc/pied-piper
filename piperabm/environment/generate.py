import numpy as np
from scipy.stats import norm

from piperabm.environment import Environment


class Generate:

    def __init__(self, environment):
        self.environment = environment
        self.fit()

    def get_pos(self):
        pos_x = []
        pos_y = []
        items = self.environment.all_nodes
        for item in items:
            item = self.environment.get_item(item)
            pos = item.pos
            pos_x.append(pos[0])
            pos_y.append(pos[1])
        return pos_x, pos_y

    def fit(self):
        pos_x, pos_y = self.get_pos()
        self.mu_x, self.sigma_x = norm.fit(pos_x)
        self.mu_y, self.sigma_y = norm.fit(pos_y)

    @property
    def gen_pos(self):
        x = list(np.random.normal(self.mu_x, self.sigma_x, 1))[0]
        y = list(np.random.normal(self.mu_y, self.sigma_y, 1))[0]
        return [x, y]
    
    @property
    def gen(self):
        env = Environment(proximity_radius=self.environment.proximity_radius)
        for i in range(len(self.environment.all_nodes)):
            pos = self.gen_pos

            


if __name__ == "__main__":

    from piperabm.environment.samples import environment_2 as env

    gen = Generate(env)
    print(gen.gen_pos)
    print(gen.gen_pos)
    #print(env.all_nodes)
    #print(g.gen_number)