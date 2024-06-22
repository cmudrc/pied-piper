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
    

if __name__ == "__main__":

    from piperabm.infrastructure import Infrastructure

    infrastructure = Infrastructure()
    infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 10])
    infrastructure.bake()
    print(infrastructure)