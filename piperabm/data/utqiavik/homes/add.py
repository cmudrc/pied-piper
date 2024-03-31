from piperabm.infrastructure_new import Infrastructure, Home
from piperabm.data.utqiavik.info import location
from piperabm.data.utqiavik.homes.generate_homes import generate_homes


def add_homes_to_infrastructure(infrastructure, settlements_num, settlement_meshes_permitted_labels='all'):
    
    homes_data = generate_homes(
        settlements_num=settlements_num,
        latitude_0=location['latitude'],
        longitude_0=location['longitude'],
        permitted_labels=settlement_meshes_permitted_labels
    )
    for home_data in homes_data:
        settlement = Home(pos=home_data)
        infrastructure.add(settlement)

    return infrastructure