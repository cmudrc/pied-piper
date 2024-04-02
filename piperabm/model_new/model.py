from piperabm.object import PureObject
from piperabm.infrastructure_new import Infrastructure
from piperabm.society_new import Society
from piperabm.economy import ExchangeRate
from piperabm.time import DeltaTime, Date, date_serialize, date_deserialize


class Model(PureObject):

    type = "model"

    def __init__(
        self,
        step_size = DeltaTime(hours=1),
        current_date: Date = Date(year=2000, month=1, day=1),
        infrastructure: Infrastructure = None,
        society = None, ####
        exchange_rate: ExchangeRate = None,
        name: str = "sample",
        path: str = None,
    ):
        super().__init__()
        self.set_step_size(step_size)
        self.current_date = current_date
        if infrastructure is None:
            infrastructure = Infrastructure()
        self.add(infrastructure)
        if exchange_rate is None:
            exchange_rate = None #####
        self.exchange_rate = exchange_rate
        self.name = name
        self.path = path

    def set_step_size(self, step_size):
        """
        Set step size
        """
        if isinstance(step_size, (float, int)):
            self.step_size = DeltaTime(seconds=step_size)
        elif isinstance(step_size, DeltaTime):
            self.step_size = step_size
        else:
            print("object not recognized")
            raise ValueError
        
    def add(self, object):
        if object.type == 'infrastructure':
            self.infrastructure = object
            self.infrastructure.model = self # Binding
        elif object.type == 'society':
            self.society = object
            self.society.model = self # Binding
        else:
            print("object not recognized")
            raise ValueError
            '''
            try:
                if object.section == "infrastructure":
                    self.infrastructure.add(object=object, id=id)
                elif object.section == "society":
                    self.society.add(object=object, id=id)
            except:
                pass
            '''

        

if __name__ == "__main__":
    pass
