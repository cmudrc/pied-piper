from piperabm.model import Model
from piperabm.infrastructure import Road

'''
roads = [
    Road(pos_1=[0, 2], pos_2=[0, 3]),
    Road(pos_1=[1, 1], pos_2=[1, 2]),
    Road(pos_1=[1, 2], pos_2=[1, 3]),
    Road(pos_1=[2, 0], pos_2=[2, 1]),
    Road(pos_1=[2, 1], pos_2=[2, 2]),
    Road(pos_1=[2, 1], pos_2=[2, 2]),
    Road(pos_1=[2, 2], pos_2=[2, 3]),
    Road(pos_1=[0, 2], pos_2=[1, 2]),
    Road(pos_1=[1, 2], pos_2=[2, 2]),
    Road(pos_1=[0, 3], pos_2=[1, 3]),
]
'''
roads = [
    Road(pos_1=[0, 0], pos_2=[0, 2]),
    Road(pos_1=[0, 2], pos_2=[2, 2]),
    Road(pos_1=[2, 2], pos_2=[2, 0]),
    Road(pos_1=[2, 0], pos_2=[0, 0]),
    Road(pos_1=[1, 0], pos_2=[1, 2]),
]

model = Model(proximity_radius=0.1)
for road in roads:
    model.add(road)



if __name__ == "__main__":
    _, log = model.infrastructure_grammar_rule_1()
    #print(log)
    _, log = model.infrastructure_grammar_rule_2()
    model.infrastructure_grammar_rule_1()
    #print(log)
    #print(len(model.all_environment_nodes))
    #print(len(model.all_environment_edges))
    model.infrastructure_grammar_rule_3()
    #infrastrucure = model.infrastrucure
    #model.print
