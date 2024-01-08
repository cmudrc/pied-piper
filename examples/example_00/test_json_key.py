from piperabm.tools.file_manager import JsonHandler as jsh
import os


dictionary = {
    'a': 'first',
    '2': 'second',
    3: 'third',
}
path = os.path.dirname(os.path.realpath(__file__))
filename = 'test'
#jsh.save(dictionary, path, filename)
data = jsh.load(path, filename)
