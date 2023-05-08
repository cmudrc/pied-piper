from piperabm import Society
from piperabm.economy import Exchange
from piperabm.resource import Resource

from environment import env


gini = 0.3
exchange_rate = Exchange()
exchange_rate.add('food', 'wealth', 10)
exchange_rate.add('water', 'wealth', 2)
exchange_rate.add('energy', 'wealth', 4)

soc = Society(env, gini=gini, exchange_rate=exchange_rate)

average_resource = Resource(
    current_resource={
        'food': 50,
        'water': 60,
        'energy': 70,
    },
    max_resource={
        'food': 80,
        'water': 90,
        'energy': 100,
    }
)
average_income = 1000
soc.generate_agents(n=10, average_resource=average_resource, average_income=average_income)


if __name__ == "__main__":
    pass
    #agents = soc.all_agents()
    #r = soc.select_best_route(agents[0], start_date, end_date)
    #print(r)