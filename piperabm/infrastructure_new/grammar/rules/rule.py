class Rule:

    def __init__(self, infrastructure, name: str):
        self.infrastructure = infrastructure
        self.name = name

    @property
    def proximity_radius(self):
        return self.infrastructure.proximity_radius
    
    def get(self, id):
        return self.infrastructure.get(id)
    
    def add(self, object):
        return self.infrastructure.add(object)
    
    def report(self, logs: list):
        if len(logs) > 0:
            print(">>>" + " " + self.name + ":")
            for log in logs:
                print(log)
        
    def check(self):
        print("NOT IMPLEMENTED YET.")

    def apply(self):
        print("NOT IMPLEMENTED YET.")

    def find(self):
        print("NOT IMPLEMENTED YET.")


class Log:

    def __init__(self, infrastructure, id, activity):
        object = infrastructure.get(id)
        self.object_info = self.create_object_info(object)
        self.activity = activity

    def create_object_info(self, object):
        txt = object.category + " " + "(" + object.type + ")" + " "
        if object.category == 'node':
            txt += "in" + " "
            txt += str(object.pos)
        elif object.category == 'edge':
            txt += "between" + " "
            txt += str(object.pos_1) + " and "
            txt += str(object.pos_2)
        return txt

    def __str__(self):
        return "  #" + " " + self.activity + ":" + " " + self.object_info
    

if __name__ == "__main__":

    from piperabm.infrastructure_new import Infrastructure, Home, Street

    infrastructure = Infrastructure()
    object_1 = Home(pos=[0, 0])
    infrastructure.add(object_1, id=1)
    object_2 = Street(pos_1=[5, 5], pos_2=[10, 10])
    infrastructure.add(object_2, id=2)

    log = Log(infrastructure, id=1, activity='add')
    print(log)
    log = Log(infrastructure, id=2, activity='add')
    print(log)