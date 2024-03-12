from piperabm.infrastructure import Settlement
from piperabm.data.utqiavik.info import location
from piperabm.data.utqiavik.settlements.generate_settlements import generate_settlements


def add_settlements_to_model(model, settlements_num, settlement_meshes_permitted_labels='all'):
    
    settlements_data = generate_settlements(
        settlements_num=settlements_num,
        latitude_0=location['latitude'],
        longitude_0=location['longitude'],
        permitted_labels=settlement_meshes_permitted_labels
    )
    for settlement_data in settlements_data:
        settlement = Settlement(pos=settlement_data)
        model.add(settlement)

    return model