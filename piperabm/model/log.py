from piperabm.log import Log, date_info


class Log(Log):
    
    def __init__(self, prefix, indentation_depth):
        super().__init__(prefix, indentation_depth)
    
    def message__burnout(self, start_date, end_date):
        txt = ''
        txt += 'BURNOUT'
        txt += ':' + ' '
        txt += date_info(start_date, end_date)
        self.add(txt)

    def message__date_step(self, start_date, end_date, current_step):
        txt = ''
        txt += 'STEP:' + ' ' + str(current_step)
        txt += ',' + ' '
        txt += date_info(start_date, end_date)
        self.add(txt)