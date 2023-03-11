from piperabm.log import Log


class Log(Log):
    
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def message__market_complete(self) -> str:
        txt = 'COMPLETED'
        self.add(txt)
        return txt
    
    def message__market_started(self) -> str:
        txt = 'STARTED'
        self.add(txt)
        return txt
    
    def message__pool_started(self, resource_name: str, stat: dict={}) -> str:
        txt = 'POOL STARTED'
        txt += ' '
        txt += '('
        txt += 'resource' + ':' + ' '
        txt += resource_name
        if 'sellers' in stat:
            txt += ',' + ' '
            txt += 'sellers'
            txt += ':' + ' '
            txt += str(stat['sellers'])
        if 'buyers' in stat:
            txt += ',' + ' '
            txt += 'buyers'
            txt += ':' + ' '
            txt += str(stat['buyers'])
        txt += ')'
        self.add(txt)
        return txt
    
    def message__pool_complete(self, resource_name: str, stat: dict={}) -> str:
        txt = 'POOL COMPLETED'
        txt += ' '
        txt += '('
        txt += 'resource' + ':' + ' '
        txt += resource_name
        if 'total_volume' in stat:
            txt += ',' + ' '
            txt += 'total_volume'
            txt += ':' + ' '
            txt += str(stat['total_volume'])
        txt += ')'
        self.add(txt)
        return txt