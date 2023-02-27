class Log:
    """
    Log important events
    """
    file_name = "log.txt"

    def __init__(self, reset=False):
        if reset is True:
            self.reset()

    def add(self, txt):
        f = open(self.file_name, "a")
        f.write(txt+'\n')
        f.close()

    def reset(self):
        f = open(self.file_name, "w")
        f.close()

    def show(self):
        result = None
        f = open(self.file_name, "r")
        result = f.read()
        f.close
        return result

    def __str__(self):
        return self.show()