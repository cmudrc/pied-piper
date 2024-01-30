from piperabm.society import Agent
from piperabm.matter.containers.samples import containers_0 as average_resources


agent = Agent(name='Peter')
agent.set_resources(average_resources)
agent.set_balance(average_balance=100)


if __name__ == '__main__':
   agent.print