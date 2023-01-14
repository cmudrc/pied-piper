class Log:
    """
    Log important events
    """
    def __init__(self, reset=False):
        self.file_name = "log.txt"
        if reset is True:
            f.open(self.file_name, "w")
        else:
            f = open(self.file_name, "a")
        f.close()

    def add(self, txt):
        f = open(self.file_name, "a")
        f.write(txt+'\n')
        f.close()