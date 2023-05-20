from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.infrastructure.settlement.samples import settlement_0


environment = Environment()

environment.append_node(
    pos=[-2, -2],
    structure=deepcopy(settlement_0)
)


if __name__ == "__main__":
    environment.print()

    '''
    from piperabm.unit import Date

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    environment.update_elements(start_date, end_date)
    current_graph = environment.to_current_graph(start_date, end_date)
    current_graph.show()
    '''