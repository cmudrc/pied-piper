from piperabm.infrastructure_new import Home
from piperabm.data.utqiavik.homes.generated_data.load import load


def add_homes_to_model(model):
    points = load()
    for point in points:
        home = Home(pos=point)
        model.add(home)
    return model


'''
from piperabm.data.utqiavik.info import location

from piperabm.data.utqiavik.homes.generated_data.generate import generate_homes

def add_homes_to_model(model, settlements_num, settlement_meshes_permitted_labels='all'):
    
    homes_data = generate_homes(
        settlements_num=settlements_num,
        latitude_0=location['latitude'],
        longitude_0=location['longitude'],
        permitted_labels=settlement_meshes_permitted_labels
    )

    for home_data in homes_data:
        settlement = Home(pos=home_data)
        model.add(settlement)

    return model
'''


if __name__ == "__main__":

    from piperabm.infrastructure_new import Infrastructure
    
    infrastructure = Infrastructure()
    infrastructure = add_homes_to_model(infrastructure)
    infrastructure.show()