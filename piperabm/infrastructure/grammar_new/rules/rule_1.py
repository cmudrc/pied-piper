from piperabm.infrastructure.grammar_new.rules.rule import Rule
from piperabm.tools.coordinate.distance import distance_point_to_point


def check(node_1, node_2, proximity_radius):
    distance = distance_point_to_point(node_1.pos, node_2.pos)
    return distance < proximity_radius


    
def infrastructure_grammar_rule_1(self):
    """
    Check for node to node proximity
    """

    anything_happened = False
    report = ['rule 1:']

    ''' loop for the first node '''
    for node_index in self.all_environment_nodes:
        ''' check if index still exist and not removed in previous rounds '''
        if node_index in self.all_environment_nodes:
            node_item = self.get(node_index)

            ''' loop for the second node '''
            for other_node_index in self.all_environment_nodes:
                ''' check if indexes still exist and not removed in previous rounds '''
                if other_node_index in self.all_environment_nodes and \
                    node_index in self.all_environment_nodes:
                    if node_index != other_node_index:
                        other_node_item = self.get(other_node_index)

                        ''' check the distance '''
                        distance = distance_point_to_point(node_item.pos, other_node_item.pos)
                        if distance < self.proximity_radius:

                            ''' update the items based on their types '''
                            if node_item.type == 'junction' and other_node_item.type != 'junction':
                                self.remove(node_item.index)
                                report.append(str(node_item) + ' removed.')
                                anything_happened = True
                            elif node_item.type == 'junction' and other_node_item.type == 'junction':
                                self.remove(node_item.index)
                                report.append(str(node_item) + ' removed.')
                                anything_happened = True
                            elif node_item.type != 'junction' and other_node_item.type == 'junction':
                                self.remove(other_node_item.index)
                                report.append(str(other_node_item) + ' removed.')
                                anything_happened = True
                            elif node_item.type != 'junction' and other_node_item.type != 'junction':
                                #print("close items are not resolved")
                                raise ValueError
                                #anything_happened = False

    return anything_happened, report

rule_1 = Rule(check=infrastructure_grammar_rule_1)