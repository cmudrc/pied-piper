from piperabm.log import Log


class Log(Log):
    
    def __init__(self, prefix, indentation_depth):
        #format_YMD = date.strftime('%Y-%m-%d')
        super().__init__(prefix, indentation_depth)
    
    def message__date_step(self, start_date, end_date, current_step, burnout=False):
        if burnout is True:
            txt = "{BURNOUT}" + ' '
        else:
            txt = ''
        txt += 'DATE:' + ' '
        txt += '['
        txt += str(start_date)
        txt += ' - '
        txt += str(end_date)
        txt += ']'
        txt += ',' + ' '
        txt += 'STEP:' + ' ' + str(current_step)
        self.add(txt)