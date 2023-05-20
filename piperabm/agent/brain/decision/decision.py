from piperabm.object import Object


class Decision(Object):

    def observe(self, environment, society) -> dict:
        """
        Agent observe itself, environment and the society
        """
        observation = {}
        print("NOT IMPLEMENTED YET")
        return observation
    
    def decide(self, observation: dict):
        print("NOT IMPLEMENTED YET")