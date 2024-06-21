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