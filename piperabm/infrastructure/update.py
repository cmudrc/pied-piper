"""
.. module:: piperabm.infrastructure.update
:synopsis: Update the infrastructure network.
"""


class Update:
    """
    Update the network
    """

    def update(self, duration: float):
        """
        Update the network
        """
        # Update degradation from age change (streets only)
        rate = 0.00001
        for ids in self.streets:
            # Update age impact
            age_impact = self.get_age_impact(ids=ids)
            age_impact += rate * duration
            self.set_age_impact(ids=ids, value=age_impact)
            # Update corresponding edge
            self.update_adjusted_length(ids=ids)


if __name__ == "__main__":

    from piperabm.society.samples.society_1 import model

    model.update(10)
    model.show()
