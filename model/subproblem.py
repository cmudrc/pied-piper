from datetime import date
import networkx as nx
import numpy as np


class Resource():
    def __init__(self, name=None, use=0, produce=0, storage_current=0, storage_max=0, deficiency_current=0, decificiency_max=0):
        self.name = name
        self.use = use
        self.produce = produce
        self.storage_current = storage_current
        self.storage_max = storage_max
        self.deficiency_current = deficiency_current
        self.deficiency_max = decificiency_max

    def __str__(self):
        return str(self.name)

    def info(self):
        result = ''
        result += 'name: ' + str(self.name) + '\n'
        result += 'use: ' + str(self.use) + '\n'
        result += 'produce: ' + str(self.produce) + '\n'
        result += 'storage_current: ' + str(self.storage_current) + '\n'
        result += 'storage_max: ' + str(self.storage_max) + '\n'
        result += 'deficiency_current: ' + str(self.deficiency_current) + '\n'
        result += 'deficiency_max: ' + str(self.deficiency_max) + '\n'
        #print(result)
        return result


class Agent():
    def __init__(self,
                 name,
                 pos,
                 alive=True,
                 resources=None
                 ):
        self.name = name
        self.pos = pos
        self.alive = alive
        self.resources = resources

    def __str__(self):
        return self.name

    def info(self):
        result = ''
        result += 'name: ' + str(self.name) + '\n'
        result += 'pos: ' + str(self.pos) + '\n'
        result += 'alive: ' + str(self.alive) + '\n'
        for resource in self.resources:
            result += resource.info()
        #print(result)
        return result

    def distance(self, other):
        x_0 = self.pos[0]
        y_0 = self.pos[1]
        x_1 = other.pos[0]
        y_1 = other.pos[1]
        return np.sqrt(np.power((x_0 - x_1), 2) + np.power((y_0 - y_1), 2))


class Model():
    def __init__(self, agents, date_now=None):
        self.agents = agents
        self.date_now = date_now

        self.last_step = 0
        self.step_size = 1

        self.G = None

    def date_to_step(self, date):
        return (self.date_now - date) / self.step_size

    def step_to_date(self, step):
        return self.date + step * self.step_size

    def distance(self, node, other_node):
        x_0 = node[1]['pos'][0]
        y_0 = node[1]['pos'][1]
        x_1 = other_node[1]['pos'][0]
        y_1 = other_node[1]['pos'][1]
        return np.sqrt(np.power((x_0 - x_1), 2) + np.power((y_0 - y_1), 2))

    def to_graph(self):
        G = nx.DiGraph()
        for agent in self.agents:
            if agent.alive is True:
                resource = agent.resources[0]
                info = {
                    'type': 'produce',
                    'name': agent.name,
                    'source': resource.produce,
                    'pos': agent.pos,
                }
                G.add_node(agent.name + '___' + info['type'], **info)
                info = {
                    'type': 'use',
                    'name': agent.name,
                    'demand': resource.use,
                    'pos': agent.pos,
                }
                G.add_node(agent.name + '___' + info['type'], **info)
                info = {
                    'type': 'storage',
                    'name': agent.name,
                    'demand': resource.storage_max - resource.storage_current,
                    'source': resource.storage_current,
                    'pos': agent.pos,
                }
                G.add_node(agent.name + '___' + info['type'], **info)
                info = {
                    'type': 'deficiency',
                    'name': agent.name,
                    'demand': resource.deficiency_current,
                    'pos': agent.pos,
                }
                G.add_node(agent.name + '___' + info['type'], **info)

            for node in G.nodes(data=True):
                for other_node in G.nodes(data=True):
                    if (node[1]['type'] == 'produce' and other_node[1]['type'] == 'use') or \
                        (node[1]['type'] == 'produce' and other_node[1]['type'] == 'storage') or \
                        (node[1]['type'] == 'produce' and other_node[1]['type'] == 'deficiency') or \
                        (node[1]['type'] == 'storage' and other_node[1]['type'] == 'use') or \
                            (node[1]['type'] == 'storage' and other_node[1]['type'] == 'deficiency'):
                        distance = self.distance(node, other_node)
                        info = {
                            'discharge': 0,
                            'distance': distance,
                        }
                        G.add_edge(node[0], other_node[0], **info)

        return G

    def run_step(self):

        step = self.last_step + 1  # current step
        print('### step: ', step)
        self.G = self.to_graph()

        while True:
            # sort edges, find the best
            scores_list = list()
            edges_list = list()

            for edge in self.G.edges(data=True):
                start = edge[0]
                end = edge[1]
                source = self.G.nodes[start]['source']
                demand = self.G.nodes[end]['demand']
                distance = edge[2]['distance']
                if source > 0 and demand > 0:
                    score = distance / demand
                    scores_list.append(score)
                    edges_list.append(edge)
            #print(len(edges_list))
            if len(edges_list) > 0:
                edges = [[edge, score] for score, edge in sorted(
                    zip(scores_list, edges_list), reverse=False)]
                order = edges[0][0]  # top offer
                #print(order)
                # make transaction, and go ahead
                self.make_transaction(order)
                # repeat until stagnation
            else:
                break

        # read them back
        for node in self.G.nodes(data=True):
            name = node[1]['name']
            type = node[1]['type']
            for agent in self.agents:
                if agent.name == name:
                    if type == 'use':
                        other = None
                        for n in self.G.nodes(data=True):
                            if n[1]['name'] == name and n[1]['type'] == 'deficiency':
                                other = n
                        # what remains from previous deficiency + deficiency from this step
                        agent.resources[0].deficiency_current = other[1]['demand'] + \
                            node[1]['demand']
                        if agent.resources[0].deficiency_current > agent.resources[0].deficiency_max:
                            agent.alive = False
                            print('ATTENTION: agent "' + agent.name + '" is dead.')
                    elif type == 'storage':
                        agent.resources[0].storage_current = (agent.resources[0].storage_max - node[1]['demand']) - (
                            agent.resources[0].storage_current - node[1]['source'])

        self.last_step = step

    def run(self, steps=1):
        for i in range(steps):
            self.run_step()

    def make_transaction(self, order):
        discharge = order[2]['discharge']
        start = order[0]
        end = order[1]
        source = self.G.nodes[start]['source']
        demand = self.G.nodes[end]['demand']
        if source >= demand:
            discharge += demand
            source -= demand
            demand = 0
        else:
            discharge += source
            demand -= source
            source = 0

        self.G.nodes[start]['source'] = source
        self.G.nodes[end]['demand'] = demand
        print('transaction ' + 'from "' + start +
              '" to "' + end + '": ' + str(discharge))


if __name__ == "__main__":
    a1 = Agent(
        name='farmer_1',
        pos=[1, 2],
        resources=[
            Resource(
                name='food',
                use=10,
                produce=10,
                storage_current=0,
                storage_max=30,
                deficiency_current=5,
                decificiency_max=10
            )
        ]
    )

    a2 = Agent(
        name='farmer_2',
        pos=[-2, -1],
        resources=[
            Resource(
                name='food',
                use=10,
                produce=10,
                storage_current=10,
                storage_max=40,
                deficiency_current=0,
                decificiency_max=15
            )
        ]
    )

    a3 = Agent(
        name='homeless_1',
        pos=[-2, 2],
        resources=[
            Resource(
                name='food',
                use=1,
                produce=0,
                storage_current=0,
                storage_max=10,
                deficiency_current=0,
                decificiency_max=10
            )
        ]
    )

    m = Model(
        agents=[a1, a2, a3],
        date_now=date.today()
    )
    m.run(15)
    #print(m.agents[0].resources[0].deficiency_current)
    #m.run_step()
    #print(a1.info())
