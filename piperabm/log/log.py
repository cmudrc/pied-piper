class Log:
    """
    Log important events
    """
    def __init__(self, reset=False):
        self.file_name = "log.txt"
        if reset is True:
            f = open(self.file_name, "w")
        else:
            f = open(self.file_name, "a")
        f.close()

    def add(self, txt):
        f = open(self.file_name, "a")
        f.write(txt+'\n')
        f.close()

'''
class Log2:
    file_name = "log.txt"
    first_call = True
    
    def __init__(self):
        if self.first_call is False:
            file = open(self.file_name, "a")
        elif self.first_call is True:
            # file exists -> reset
            # or else create it
            f = open(self.file_name, "w")
            self.first_call = False

    def add(self, txt):
        f = open(self.file_name, "a")
        f.write(txt+'\n')
        f.close()
'''