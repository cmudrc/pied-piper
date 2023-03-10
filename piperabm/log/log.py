class Log:
    """
    Log important events
    """
    file_name = "log.txt"

    def __init__(self):
        pass

    def add(self, txt):
        """
        Add new data as text to log file
        """
        f = open(self.file_name, "a")
        f.write(txt+'\n')
        f.close()

    def reset(self):
        """
        Reset the log file
        """
        f = open(self.file_name, "w")
        f.close()

    def show(self):
        """
        Show the materials within the log file
        """
        result = None
        f = open(self.file_name, "r")
        result = f.read()
        f.close
        return result

    def __str__(self):
        return self.show()
    

if __name__ == "__main__":
    log = Log()
    log.reset()
    log.add("Hello World!")