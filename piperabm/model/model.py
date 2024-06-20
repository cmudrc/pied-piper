from piperabm.model.serialize import Serialize
from piperabm.model.file import File
from piperabm.model.update import Update
from piperabm.infrastructure import Infrastructure
from piperabm.society import Society


class Model(
    Serialize,
    File,
    Update
):
    """
    Main class of simulation
    """

    type = "model"

    def __init__(
        self,
        name: str = 'model',
        path=None
    ):
        super().__init__()
        self.time = 0
        self.step = 0
        self.infrastructure = Infrastructure()
        self.infrastructure.model = self # Binding
        self.society = Society()
        self.society.model = self # Binding
        self.name = name
        self.path = path # File saving

    def bake(
            self,
            save: bool = False,
            proximity_radius: float = 0,
            search_radius: float = None,
            report: bool = False
        ):
        """
        Bake model
        """
        self.infrastructure.bake(
            report=report,
            proximity_radius=proximity_radius,
            search_radius=search_radius
        )
        if save is True:
            self.save(state='infrastructure')

    
if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.infrastructure.add_street(pos_1=[-5, 0], pos_2=[5, 0])
    model.bake()
    print(model.infrastructure)
    '''
    from piperabm.society.samples import model_1 as model
    

    agent_id = 1
    destination_id = 2
    print(model.society.alive_agents)
    model.society.go_and_comeback(agent_id, destination_id)

    data = model.serialize()

    from piperabm.tools.file_manager import JsonFile
    import os

    path = os.path.dirname(os.path.realpath(__file__))
    file = JsonFile(path, filename='test')
    file.save(data)
    data_new = file.load()
    file.remove()
    model_new = Model()
    model_new.deserialize(data_new)
    #print(model==model_new)
    #model.update(1000)
    #print(model.society.serialize()['G'][1])
    #print(model.society.G.nodes[1])
    #print(model_new.society.serialize()['G'])
    #print(model.society.G.nodes[1])
    #print(model_new.society.G.nodes[1])
    #print(model_new.society.G.nodes(1))
    model_new.update(10000000)
    print(model_new.society.alive_agents)
    '''
