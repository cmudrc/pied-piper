from piperabm.log import Log, agent_info


class Log(Log):
    
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def message__transaction(
            self,
            from_agent_index,
            to_agent_index,
            amount,
            from_agent_name='',
            to_agent_name=''
        ):
        txt = "from: " + agent_info(
            agent_index=from_agent_index,
            agent_name=from_agent_name
        )
        txt += ", to: " + agent_info(
            agent_index=to_agent_index,
            agent_name=to_agent_name
        )
        txt += ", amount: " + str(amount)
        self.add(txt)
        return txt

    def message__participants(
            self,
            sellers,
            buyers
    ):
        txt = ''
        txt += 'sellers: ' + str(sellers)
        txt += 'buyers: ' + str(buyers)
        self.add(txt)
        return txt
    
    def message__pool_complete(self):
        txt = 'COMPLETED'
        self.add(txt)
        return txt
    
    def message__pool_started(self):
        txt = 'STARTED'
        self.add(txt)
        return txt