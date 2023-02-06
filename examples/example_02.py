from piperabm import Model, Environment, Society
from piperabm.unit import Date, DT

''' Create environment '''
env = Environment(links_unit_length=10)

## Add a sample settlement
env.add_settlement(
    name="Settlement",
    pos=[-500, 0],
)
## Add a sample market
env.add_market(
    name="Market",
    pos=[500, 0]
)
## Add a connecting link between elements
env.add_link(start="Settlement", end="Market")

## Preview sample environemnt
#env.show(start_date=Date.today(), end_date=Date.today()+DT(days=1))

''' Create society '''
society = Society(env)

## Add sample person
from piperabm.actions import Queue, Move, Walk

## Create a sample action queue
queue = Queue()
move = Move(
    start_date=Date.today(),
    start_pos=[-1800, 0],
    end_pos=[1800, 0],
    transportation=Walk()
)
print(move.start_date, move.end_date)
queue.add(move)
society.add_agent(
    name="Person",
    queue=queue
)

''' Create model '''
m = Model(
    environment=env,
    society=society,
    step_size=DT(seconds=360)
)

agent = m.society.G.nodes[0]
for i in range(10):
    m.run()
    print(agent['pos'])
#    m.show()