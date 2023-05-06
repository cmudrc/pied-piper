from piperabm.society.relationship import Family, Neighbor, FellowCitizen


def load_relationship(dictionary: dict):
    relationship = None
    type = dictionary['type']
    if type == 'family':
        relationship = Family()
    elif type == 'neighbor':
        relationship = Neighbor()
    elif type == 'fellow citizen':
        relationship = FellowCitizen()
    relationship.from_dict(dictionary)
    return relationship
