from piperabm.tools import find_element


class Link:

    def __init__(self, origin, destination, all_elements, path=None):
        if isinstance(agent, ):
            origin_name = origin
        if isinstance(origin, str):
            origin_name = origin
        else:
            origin_name = origin
        agent = find_element(origin_name, all_elements)
        self.origin = origin
        self.destination = destination
        self.path = path


if __name__ == "__main__":
    from piperabm.asset import Asset, Resource, Storage, Produce


    element = Asset(
        resources=[
            Resource(
                name='food',
                storage=Produce(
                    rate=1
                )
            )
        ]
    )
    origin = Asset(
        resources=[
            Resource(
                name='food',
                storage=Storage(
                    current_amount=0,
                    max_amount=10
                )
            )
        ]
    )

    element.refill(10, mode='dependent', resource=origin.resource('food'))
    element.show()
    #origin
