import matplotlib.pyplot as plt

from pr.graphics.plt.boundery import boundery_to_plt
from pr.graphics.plt.agent import agent_to_plt
from pr.tools import find_element


def settlement_to_plt(dictionary: dict, ax=None, all_agents=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary

    if d['boundery'] is not None:
        boundery_to_plt(d['boundery'], ax, d['active'])
    
    #if all_agents is not None:
    #    for agent_name in d['agents']:
    #        agent = find_element(agent_name, all_agents)
    #        agent_to_plt(agent.to_dict(), ax)
