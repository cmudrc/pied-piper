import os

from piperabm.model import Model


model = Model(name='Sample Model')
model.path = os.path.dirname(os.path.realpath(__file__))
model.load_initial()


if __name__ == "__main__":
    print("infrastructure nodes: " + str(len(model.infrastructure_nodes)))
    print("infrastructure edges: " + str(len(model.infrastructure_edges)))
    print("society nodes: " + str(len(model.society_nodes)))
    print("society edges: " + str(len(model.society_edges)))
    agent = model.get(0)
    print(agent.queue)
    #print()
    #model.update(save=False)
    #print(model)
    #model.show()
    '''
    from piperabm.tools import Delta
    from copy import deepcopy

  m,    #print(object.pos)
    old = deepcopy(model.old)
    old_model = deepcopy(model)
    model.run(n=1)
    new = model.serialize()
    delta = Delta.create(old, new)
    old_model.apply_delta(delta)
    print(old_model == model)
    #print(model.old)
    #object = model.get(0)
    #print(object.pos)
    '''