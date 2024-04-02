import networkx as nx
from copy import deepcopy
import random
import uuid




class Query:

    def get(self, id: int):
        """
        Get object by its id
        """
        return self.library[id]

    @property
    def all(self):
        """
        Return id of all items
        """
        return self.library.keys()
    
    @property
    def new_id(self) -> int:
        """
        Generate a new unique integer as id for graph items
        """
        result = None
        while True:
            new_id = uuid.uuid4().int
            if self.has_id(new_id) is False:
                result = new_id
                break
        return result
    
    def has_id(self, id: int) -> bool:
        """
        Check if the id already exists
        """
        result = False
        if id in self.all:
            result = True
        return result
    
    def add(self, object, id: int = None):
        """
        Add new object to infrastructure
        """
        # ID
        if id is None:
            id = self.new_id
        else:
            if self.has_id(id) is True:
                id = self.new_id
        # Add Node
        if object.category == "node":
            object.society = self # Binding
            # Assign home
            infrastructure = self.infrastructure
            if infrastructure is None:
                print("infrastructure not found")
                raise ValueError
            homes = infrastructure.homes
            if object.home is None:
                object.home = random.choice(homes)
            else:
                if object.home not in homes:
                    raise ValueError
            # Assign location
            home = self.infrastructure.get(object.home)
            object.current_node = deepcopy(object.home)
            object.pos = deepcopy(home.pos)
            object.id = id
            self.library[id] = object
            self.G.add_node(id)
        else:
            print("Object type not recognized.")
            raise ValueError
        return id