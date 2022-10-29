import unittest


def discover(target:str='all'):
    suite = None
    loader = unittest.TestLoader()
    TEST_DIR = 'test'
    if target == 'all':
        suite = loader.discover(TEST_DIR)
    else:
        pattern = TEST_DIR + '_' + target + '.py'
        suite = loader.discover(TEST_DIR, pattern)
    return suite
    
def test(target:str='all'):
    suite = discover(target)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    

if __name__ == "__main__":
    test('all')