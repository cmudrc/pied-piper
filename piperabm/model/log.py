from piperabm.log import Log


class Log(Log):
    
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def message__date_step(self, start_date, end_date, current_step, burnout=False):
        if burnout is True:
            txt = "{BURNOUT}" + ' '
        else:
            txt = ''
        txt += 'DATE:' + ' '
        txt += '['
        txt += str(start_date.strftime('%Y-%m-%d'))
        txt += '-'
        txt += str(end_date.strftime('%Y-%m-%d'))
        txt += ']'
        txt += ',' + ' '
        txt += 'STEP:' + ' ' + str(current_step)
        self.add(txt)