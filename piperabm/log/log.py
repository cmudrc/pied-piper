class Log:
    def __init__(self):
        self.file_name = "log.txt"
        f = open(self.file_name, "w")
        f.close()
    def add(self, txt):
        f = open(self.file_name, "a")
        f.write(txt+'\n')
        f.close()