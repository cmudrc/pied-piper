from piperabm.object import PureObject
from piperabm.environment.add import Add, Validate
from piperabm.environment.query import Query, Search, Filter


class Environment(
    PureObject,
    Add,
    Validate,
    Query,
    Search,
    Filter
):

    def __init__(self):
        self.items = {}


if __name__ == '__main__':
    from piperabm.environment import Settlement, Junction

    settlement = Settlement(
        id='1',
        name='sample settlement',
        pos=[0, 0],
    )
    junction = Junction(
        id='2',
        name='sample junction',
        pos=[1, 1],
    )
    env = Environment()
    env.add([settlement, junction])
    print(env.get_item_by_id('1'))