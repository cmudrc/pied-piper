from piperabm.log import Log


class Log(Log):
    
    def __init__(self, prefix, indentation_depth):
        super().__init__(prefix, indentation_depth)
    
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
        txt += ':'
        txt += ' '
        txt += resource_name
        if len(stat) > 0:
            txt += ' '
            txt += '('
            if 'sellers' in stat:
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
        txt += ':'
        txt += ' '
        txt += resource_name
        if len(stat) > 0:
            txt += ' '
            txt += '('
            if 'total_volume' in stat:
                txt += 'total_volume'
                txt += ':' + ' '
                txt += str(stat['total_volume'])
            txt += ')'
        self.add(txt)
        return txt