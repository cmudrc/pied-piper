import unittest


class Test:
    """
    Run tests in batch
    """
    def __init__(self, directory='test'):
        self.directory = directory
        self.loader = unittest.TestLoader()
        self.runner = unittest.TextTestRunner()

    def discover(self, target: str):
        suite = None
        if target == 'all':
            suite = self.loader.discover(self.directory)
        else:
            pattern = self.directory + '_' + target + '.py'
            suite = self.loader.discover(self.directory, pattern)
        return suite
    
    def run(self, target: str = 'all'):
        suite = self.discover(target)
        self.runner.run(suite)
    

if __name__ == "__main__":
    test = Test()
    test.run('all')