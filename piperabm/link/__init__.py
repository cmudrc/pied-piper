from piperabm.search import find_element


class InstantLink:

    def __init__(self, origin, destination, all, path=None):
        if isinstance(agent, ):
            origin_name = origin
        if isinstance(origin, str):
            origin_name = origin
        else:
            origin_name = origin
        agent = find_element(origin_name, self.all)
        self.origin = origin
        self.destination = destination
        self.path = path

    
if __name__ == "__main__":
    from piperabm.asset import Asset, Resource, Storage, Produce


    a_1 = Asset(
        resources=Resource(
            name='food',
            storage=Storage(
                current_amount=20,
                max_amount=20
            )
        )
    )

    a_1.show()