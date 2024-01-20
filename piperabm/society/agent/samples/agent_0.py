from piperabm.society import Agent
from piperabm.matter.containers.samples import containers_0 as resources


agent = Agent(
    name='Peter',
    resources=resources,
    balance=200,
    income=200 / (24*60*600*30) # monthly
)


if __name__ == '__main__':
   agent.print