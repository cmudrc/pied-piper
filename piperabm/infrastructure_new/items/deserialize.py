from piperabm.infrastructure_new.items.junction import Junction
from piperabm.infrastructure_new.items.home import Home
from piperabm.infrastructure_new.items.market import Market
from piperabm.infrastructure_new.items.street import Street
from piperabm.infrastructure_new.items.neighborhood_access import NeighborhoodAccess


def infrastructure_deserialize(dictionary):
    if dictionary["type"] == "junction":
        object = Junction()
    elif dictionary["type"] == "home":
        object = Home()
    elif dictionary["type"] == "market":
        object = Market()
    elif dictionary["type"] == "street":
        object = Street()
    elif dictionary["type"] == "neighborhood_access":
        object = NeighborhoodAccess()
    else:
        print("object not recognized")
        raise ValueError
    object.deserialize(dictionary)
    return object