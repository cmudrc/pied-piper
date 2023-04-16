from piperabm.environment import Environment
from piperabm.environment.elements.samples import hub_0


environment = Environment(links_unit_length=10)
index = environment.find_next_index()
environment.add_node(index, element=hub_0)


if __name__ == "__main__":
    print(environment)
    
    #from piperabm.unit import Date

    #start_date = Date(2020, 1, 5)
    #end_date = Date(2020, 1, 10)
    #environment.update_elements(start_date, end_date)
    #current_graph = environment.to_link_graph(start_date, end_date)
    #current_graph.show()
