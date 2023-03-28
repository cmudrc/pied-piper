def calculate_fuel_factor(society, path_graph, agent, route):
    """
    Ratio of required fuel until destination to agent's current resource
    """
    resource = society.agent_info(agent, 'resource')
    transportation = society.agent_info(agent, 'transportation')
    path = path_graph.edge_info(route[0], route[1], 'path')
    fuel = path.total_fuel(transportation)
    result = fuel / resource
    return result(result.max())


if __name__ == "__main__":
    from piperabm.society.sample import soc_1 as soc
    from piperabm.unit import Date, DT

    agents = soc.all_agents()
    agent = agents[0]
    start_date = Date.today() + DT(days=1)
    end_date = start_date + DT(days=1)
    path_graph = soc.env.to_path_graph(start_date, end_date)
    #path_graph.show()
    route = (0, 1)
    factor = calculate_fuel_factor(
        society=soc,
        path_graph=path_graph,
        agent=agent,
        route=route
    )
    print(factor)