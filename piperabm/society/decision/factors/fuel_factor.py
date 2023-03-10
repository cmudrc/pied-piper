def calculate_fuel_factor(society, path_graph, agent, route):
    """
    Ratio of required fuel until destination to agent's current resource
    """
    resource = society.agent_info(agent, 'resource')
    transportation = society.agent_info(agent, 'transportation')
    path = path_graph.edge_info(route[0], route[1], 'path')
    fuel = path.total_fuel(transportation)
    result = fuel / resource
    print(result)
    return result


if __name__ == "__main__":
    #from piperabm.society.sample import soc_1 as soc
    from piperabm.unit import Date

    #path_graph = soc.env.to_path_graph(start_date=Date(2020, 1, 3), end_date=Date(2020, 1, 5))
    agent = 1
    #path_graph.agent_info(agent, 'settlement')
    route = (0, 1)
    #calculate_fuel_factor(soc, path_graph, agent, route)