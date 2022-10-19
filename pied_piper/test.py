import unittest


def test(target:str='all'):
    suite = None
    loader = unittest.TestLoader()
    start_dir = 'test'
    if target == 'all':
        suite = loader.discover(start_dir)
    else:
        pattern = start_dir + '_' + target + '.py'
        suite = loader.discover(start_dir, pattern=pattern)
    return suite
    

if __name__ == "__main__":
    #target = 'settlement'
    target = 'all'
    suite = test(target=target)
    runner = unittest.TextTestRunner()
    runner.run(suite)