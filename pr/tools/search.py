def find_element(name, all_elements):
    """
    Find an element between a list of elements based on its name property
    """
    result = None
    for element in all_elements:
        if element.name == name:
            result = element
            break
    return result


if __name__ == "__main__":
    from pr.agent import Agent
    a_1 = Agent(name='agent_1')
    a_2 = Agent(name='agent_2')
    all_agents = [
        a_1,
        a_2,
    ]

    agent = find_element('agent_2', all_elements=all_agents)
    print(agent.name)