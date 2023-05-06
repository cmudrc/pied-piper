from piperabm.unit import Date, DT
from piperabm.environment.samples import env_1 as env
from piperabm import Society
from piperabm.economy import Exchange
from piperabm import Resource


gini = 0.3
exchange_rate = Exchange()
exchange_rate.add('food', 'wealth', 10)
exchange_rate.add('water', 'wealth', 2)
exchange_rate.add('energy', 'wealth', 4)
soc = Society(env, gini=gini, exchange_rate=exchange_rate)
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
average_income = 1000
soc.generate_agents(
    n=5,
    average_resource=average_resource,
    average_income=average_income
)


if __name__ == "__main__":
    print(soc)