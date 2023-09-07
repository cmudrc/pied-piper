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

    s_1 = Settlement(
        id='1',
        name='settlement 1',
        pos=[0, 0],
    )
    env = Environment()
    env.add(s_1)
    #print(env.items['1'])
    #print(env.get_item_by_id('1'))