from piperabm import Environment, Society, Model
from piperabm.economy import Exchange
from piperabm.resource import Resource
from piperabm.measure import Accessibility, TravelLength
from piperabm.unit import Date, DT

''' Environmet '''
env = Environment(links_unit_length=10)
env.add_settlement(name="Settlement 1", pos=[-60, 40], initiation_date=Date(2020, 1, 2))
env.add_settlement(name="Settlement 2", pos=[200, 20], initiation_date=Date(2020, 1, 1))
env.add_settlement(name="Settlement 3", pos=[100, -180], initiation_date=Date(2020, 1, 1))
env.add_link(start="Settlement 1", end=[0, 0], initiation_date=Date(2020, 1, 1))
env.add_link(start=[0.1, 0.1], end=[80, 60], initiation_date=Date(2020, 1, 1))
env.add_link(start=[80, 60], end=[200, 20], initiation_date=Date(2020, 1, 1))
env.add_link(start=[0, 0], end="Settlement 3", initiation_date=Date(2020, 1, 1))

#start_date = Date(2020, 1, 1)
#end_date = start_date + DT(hours=12)
#env.show(start_date, end_date)
#path_graph = env.to_path_graph(start_date, end_date)
#path_graph.show()

''' Society '''
gini = 0.3
average_income = 1000
exchange_rate = Exchange()
exchange_rate.add('food', 'wealth', 10)
exchange_rate.add('water', 'wealth', 2)
exchange_rate.add('energy', 'wealth', 4)
soc = Society(env, gini=gini, average_income=average_income, exchange_rate=exchange_rate)
average_resource = Resource(
    current_resource={
        'food': 20,
        'water': 40,
        'energy': 60,
    },
    max_resource={
        'food': 100,
        'water': 200,
        'energy': 300,
    }
)
soc.add_agents(n=5, average_resource=average_resource)

#agents = soc.all_agents()
#r = soc.select_best_route(agents[0], start_date, end_date)
#print(r)

''' Model '''
m = Model(
    society=soc,
    step_size=DT(hours=12),
    current_date=Date(2020, 1, 1)
)
m.add_measures([Accessibility(), TravelLength()])
print(soc.agent_info(1, 'resource'), soc.agent_info(1, 'active'))
m.run(2)
print(soc.agent_info(1, 'resource'), soc.agent_info(1, 'active'))
#m.measures.show()