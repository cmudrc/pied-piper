from piperabm.society_new.agent.agent import Agent


def society_deserialize(dictionary, society):
    if dictionary["type"] == "agent":
        object = Agent()
        object.society = society
    else:
        print("object not recognized")
        raise ValueError
    object.deserialize(dictionary)
    return object