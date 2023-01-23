from piperabm import Model, Environment, Society
from piperabm.unit import Date, DT

''' Create environment '''
env = Environment(links_unit_length=10)

## Add a sample settlement
env.add_settlement(
    name="Settlement",
    pos=[-50, 0]
)
## Add a sample market
env.add_market(
    name="Market",
    pos=[50, 0]
)
## Add a connecting link between elements
env.add_link(start="Settlement", end="Market")

## Preview sample environemnt
#env.show(start_date=Date.today(), end_date=Date.today()+DT(days=1))

society = Society(env)
society.add_agent()