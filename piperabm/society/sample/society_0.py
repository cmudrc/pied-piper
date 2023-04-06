from piperabm import Society
from piperabm.economy.exchange.sample import exchange_0
from piperabm.environment.sample import env_0
from piperabm.society.agent.sample import sample_agent_0, sample_agent_1


society = Society(
    env=env_0,
    gini=0.3,
    exchange_rate=exchange_0
)
agents = [sample_agent_0, sample_agent_1]
society.add(agents)


if __name__ == "__main__":
    from piperabm.unit import Date

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    society.env.update_elements(start_date, end_date)
    link_graph = society.env.to_link_graph(start_date, end_date)
    link_graph.show()
