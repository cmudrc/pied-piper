import unittest


class Test:
    """
    Run tests in batch
    """

    def __init__(self, TEST_DIR='test'):
        self.TEST_DIR = TEST_DIR
        self.loader = unittest.TestLoader()
        self.runner = unittest.TextTestRunner()

    def discover(self, target: str):
        suite = None
        loader = self.loader
        TEST_DIR = self.TEST_DIR
        if target == 'all':
            suite = loader.discover(TEST_DIR)
        else:
            pattern = TEST_DIR + '_' + target + '.py'
            suite = loader.discover(TEST_DIR, pattern)
        return suite
    
    def run(self, target: str='all'):
        suite = self.discover(target)
        self.runner.run(suite)
    

if __name__ == "__main__":
    test = Test(TEST_DIR='test')
    #test.run('all')
    test.run('move')