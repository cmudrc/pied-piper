from piperabm.unit import Date
from piperabm.economy import Economy


class Update:
    """
    Contains methods for Society class
    Methods for updating agents in each step
    """

    def update_elements(self, start_date: Date, end_date: Date):
        """
        Update all agents between *start_date* and *end_date*
        """

        agents_indexes = self.all_indexes()
        for index in agents_indexes:
            agent = self.get_agent_object(index)
            agent.update(start_date, end_date)
