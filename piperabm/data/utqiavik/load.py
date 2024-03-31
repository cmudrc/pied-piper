from piperabm.data.utqiavik.streets import add_streets_to_model
from piperabm.data.utqiavik.homes import add_homes_to_model


def add_to_model(model):
    model = add_streets_to_model(model)
    #model.bake()
    #model = add_homes_to_model(model)
    return model


if __name__ == "__main__":

    from piperabm.infrastructure_new import Infrastructure
    
    infrastructure = Infrastructure()
    infrastructure = add_to_model(infrastructure)
    infrastructure.bake(report=True)
    print(infrastructure.stat)
    
    #infrastructure.show()