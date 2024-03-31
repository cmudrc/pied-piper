from piperabm.infrastructure_new import Street
from piperabm.data.utqiavik.streets.read_streets import read_streets
from piperabm.data.utqiavik.info import location


def add_streets_to_model(model, streets_permitted_labels='all'):
    streets_data = read_streets(
        latitude_0=location['latitude'],
        longitude_0=location['longitude'],
        permitted_labels=streets_permitted_labels
    )
    for street_data in streets_data:
        street = Street(
            pos_1=street_data['pos_1'],
            pos_2=street_data['pos_2'],
            name=street_data['name']
        )
        model.add(street)
    return model


if __name__ == "__main__":

    from piperabm.infrastructure_new import Infrastructure
    from piperabm.data.utqiavik.streets.labels import map_1 as permitted_labels

    infrastructure = Infrastructure()
    infrastructure = add_streets_to_model(infrastructure, streets_permitted_labels=permitted_labels)
    infrastructure.bake()
    infrastructure.show()
