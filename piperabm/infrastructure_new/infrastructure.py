import networkx as nx

from piperabm.object import PureObject
from piperabm.infrastructure_new.query import Query
from piperabm.infrastructure_new.graphics import Graphics
from piperabm.infrastructure_new.grammar import Grammar
from piperabm.infrastructure_new.paths import Paths
from piperabm.infrastructure_new.items.deserialize import infrastructure_deserialize
from piperabm.tools.file_manager import JsonFile


class Infrastructure(PureObject, Query, Graphics):

    type = "infrastructure"

    def __init__(self):
        super().__init__()
        self.G = nx.Graph()
        self.model = None # Bind
        self.library = {}
        self.baked = True
        self.path = None

    def bake(
            self,
            save: bool = False,
            name: str = 'infrastructure',
            report: bool = False,
            proximity_radius: float = 1,
            search_radius: float = None
        ):
        if self.baked is False:
            grammar = Grammar(
                infrastructure=self,
                save=save,
                name=name,
                proximity_radius=proximity_radius,
                search_radius=search_radius
            )
            grammar.apply(report=report)
            print("baking is done.")
        else:
            print("already baked.")

    @property
    def stat(self):
        result = {
            'node': {
                'junction': len(self.junctions),
                'home': len(self.homes),
                'market': len(self.markets),
            },
            'edge': {
                'street': len(self.streets),
                'neighborhood_access': len(self.neighborhood_accesses),
            },
        }
        return result
    
    def show_stat(self):
        stat = self.stat
        for category in stat:
            for name in stat[category]:
                print("# " + name + ": " + str(stat[category][name]))
    
    def current(self):
        """
        Current state of infrastructure with edge weights showing the adjusted_length
        """
        G = nx.Graph()
        nodes = self.nodes_id
        for id in nodes:
            object = self.get(id)
            G.add_node(id)
        edges_id = self.edges_id
        for id in edges_id:
            ids = self.edge_ids(id)
            object = self.get(id)
            G.add_edge(
                ids[0],
                ids[1],
                id=id,
                adjusted_length=object.adjusted_length
            )
        return G
    
    def paths(self):
        """
        Paths graph
        """
        return Paths(infrastructure=self)

    def save(self, name: str = 'infrastructure'):
        """
        Save infrastructure to file
        """
        data = self.serialize()
        file = JsonFile(self.path, filename=name)
        file.save(data)

    def load(self, name: str = 'infrastructure'):
        """
        Load infrastructure from file
        """
        file = JsonFile(self.path, filename=name)
        data = file.load()
        self.deserialize(data)

    def serialize(self):
        dictionary = {}
        library_serialized = {}
        for id in self.all:
            object = self.get(id)
            library_serialized[id] = object.serialize()
        dictionary['library'] = library_serialized
        dictionary['G'] = nx.to_dict_of_dicts(self.G)
        dictionary['baked'] = self.baked
        dictionary['type'] = self.type
        return dictionary

    def deserialize(self, dictionary):
        library_serialized = dictionary['library']
        for id in library_serialized:
            object = infrastructure_deserialize(library_serialized[id])
            self.library[int(id)] = object
        converted_dict_of_dicts = {
            int(outer_key): {int(inner_key): values for inner_key, values in outer_dict.items()}
            for outer_key, outer_dict in dictionary['G'].items()
        }
        self.G = nx.from_dict_of_dicts(d=converted_dict_of_dicts)
        self.baked = dictionary['baked']


if __name__ == "__main__":

    from piperabm.infrastructure_new import Street

    infrastructure = Infrastructure(
        model=None,
        proximity_radius=1
    )
    street = Street(pos_1=[0, 0], pos_2=[10, 10])
    infrastructure.add(street)
    infrastructure.bake()
    print(infrastructure)