from piperabm.unit import Date
#from piperabm.economy import Economy


class Update:
    """
    Contains methods for Society class
    Methods for updating agents in each step
    """

    def update(self, start_date: Date, end_date: Date):
        """
        Update all agents between *start_date* and *end_date*
        """
        ''' filter current elements '''
        self.to_current_graph(start_date, end_date)

        for index in self.current.all_indexes():
            agent = self.get_agent_object(index)
            agent.update(start_date, end_date)
