from piperabm.log import Log


class Log(Log):
    
    def __init__(self):
        super().__init__()
    
    def message__date_step(self, start_date, end_date, current_step, burnout=False):
        if burnout is True:
            txt = '##### Burnout #####' + '\n'
        else:
            txt = ''
        txt += '>>> date: '
        txt += '['
        txt += str(start_date.strftime('%Y-%m-%d'))
        txt += '-'
        txt += str(end_date.strftime('%Y-%m-%d'))
        txt += ']'
        txt += ', '
        txt += 'step: ' + str(current_step)
        self.add(txt)