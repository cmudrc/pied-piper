from load import model
from data.info import agents_num


model.generate_agents(num=agents_num)
model.save_initial()