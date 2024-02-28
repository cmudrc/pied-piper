from piperabm.society.agent.agent import Agent
from piperabm.society.relationships.family import Family


def society_deserialize(dictionary, model):
    if dictionary["type"] == "agent":
        object = Agent()
    elif dictionary["type"] == "family":
        object = Family()
    object.deserialize(dictionary)
    object.model = model
    return object