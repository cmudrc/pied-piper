from piperabm.tools.file_manager import JsonHandler as jsh
import os


path = os.path.dirname(os.path.realpath(__file__))
filename = 'test'

data = {
    '1': 'first',
    2: 'second',
}
print(data['1'])
print(data[2])

jsh.save(data, path, filename)
data = jsh.load(path, filename)
print(data['1'])
print(data[2])
