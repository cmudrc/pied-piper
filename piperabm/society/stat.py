from piperabm.tools.print.stat import Print


class Stat(Print):
    """
    Stats of the network
    """
    
    @property
    def stat(self):
        """
        Return stats of the network
        """
        return {
            "node": {
                "alive": len(self.alives),
                "dead": len(self.deads),
                "total": len(self.agents),
            },
            "edge": {
                "family": len(self.families),
                "friend": len(self.friends),
                "neighbor": len(self.neighbors),
            },
        }
    

if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.bake()
    model.society.generate(num=1)

    print(model.society)