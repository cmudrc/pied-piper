import os

from load import model


model.path = os.path.dirname(os.path.realpath(__file__))
measures = model.measure()
accessibility = measures['accessibility']
#accessibility.show()
ids = model.society.agents
#print(accessibility.library[ids[50]])
#print(accessibility.average(agents=ids[50], resources='food'))
#print(accessibility.extract(agent=ids[50], resource='food', time_step=10))
#data = accessibility.organize_data(agents=[ids[49], ids[50]], resources='food')
#print(data.keys())
accessibility.show(agents='all', resources='all', average=False)