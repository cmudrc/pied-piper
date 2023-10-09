from piperabm.environment.items import Road
from piperabm.tools.coordinate.distance import distance_point_to_point, distance_point_to_line
from piperabm.tools.coordinate.intersect import intersect_line_line


class Grammar:
    
    def apply_grammars(self, report=False):
        """
        Apply all grammars based on a decision tree
            if a rule is not yielding any changes, it is ok to go the next rule.
            if not, all grammars rules start over.
            if no next rule is available, the program is over.
        """
        grammars = [
            self.grammar_rule_1,
            self.grammar_rule_2,
            self.grammar_rule_3,
            self.grammar_rule_4
        ]

        i = 0
        while True:
            anything_happened, log = grammars[i]()

            if report is True:
                print(log)

            if anything_happened is True:
                i = 0  # reset to the loop
            else:
                i += 1  # move to the next grammar

            if i == len(grammars):
                break  # exit if all grammars are applied without any changes
        
    def grammar_rule_1(self):
        """
        Check for node to node proximity
        """

        anything_happened = False
        report = ['rule 1:']

        ''' loop for the first node '''
        for node_index in self.all_nodes:
            ''' check if index still exist and not removed in previous rounds '''
            if node_index in self.all_nodes:
                node_item = self.get_item(node_index)

                ''' loop for the second node '''
                for other_node_index in self.all_nodes:
                    ''' check if indexes still exist and not removed in previous rounds '''
                    if other_node_index in self.all_nodes and \
                        node_index in self.all_nodes:
                        if node_index != other_node_index:
                            other_node_item = self.get_item(other_node_index)

                            ''' check the distance '''
                            distance = distance_point_to_point(node_item.pos, other_node_item.pos)
                            if distance < self.proximity_radius:

                                ''' update the items based on their types '''
                                if node_item.type == 'junction' and other_node_item.type != 'junction':
                                    self.remove_item(node_item.index)
                                    report.append(str(node_item) + ' removed.')
                                    anything_happened = True
                                elif node_item.type == 'junction' and other_node_item.type == 'junction':
                                    self.remove_item(node_item.index)
                                    report.append(str(node_item) + ' removed.')
                                    anything_happened = True
                                elif node_item.type != 'junction' and other_node_item.type == 'junction':
                                    self.remove_item(other_node_item.index)
                                    report.append(str(other_node_item) + ' removed.')
                                    anything_happened = True
                                elif node_item.type != 'junction' and other_node_item.type != 'junction':
                                    #print("close items are not resolved")
                                    raise ValueError
                                    #anything_happened = False

        return anything_happened, report

    def grammar_rule_2(self):
        """
        Check for node to edge proximity
        """

        anything_happened = False
        report = ['rule 2:']

        ''' loop for the node '''
        for node_index in self.all_nodes:
            if node_index in self.all_nodes: # to make sure it is not deleted in previous runs
                node_item = self.get_item(node_index)

                ''' loop for the edge '''
                for edge_index in self.all_edges:
                    if edge_index in self.all_edges and node_index in self.all_nodes: # to make sure it is not deleted in previous runs
                        edge_item = self.get_item(edge_index)
                        #print(edge_item.pos_1, edge_item.pos_2)

                        ''' check the distance '''
                        distance = distance_point_to_line(node_item.pos, edge_item.pos_1, edge_item.pos_2)
                        distance_1 = distance_point_to_point(node_item.pos, edge_item.pos_1)
                        distance_2 = distance_point_to_point(node_item.pos, edge_item.pos_2)
                        if distance is not None and \
                            distance < self.proximity_radius and \
                            distance_1 > self.proximity_radius and \
                            distance_2 > self.proximity_radius:
                                    
                            ''' update the items based on their types '''
                            if edge_item.type == 'road':
                                new_edge_item_1 = Road(pos_1=edge_item.pos_1, pos_2=node_item.pos)
                                new_edge_item_2 = Road(pos_1=node_item.pos, pos_2=edge_item.pos_2)
                            self.add(new_edge_item_1)
                            report.append(str(new_edge_item_1) + ' added.')
                            self.add(new_edge_item_2)
                            report.append(str(new_edge_item_2) + ' added.')
                            self.remove_item(edge_index)
                            report.append(str(edge_item) + ' removed.')
                            anything_happened = True

        return anything_happened, report

    def grammar_rule_3(self):
        """
        Check for edge to edge intersection
        """
        anything_happened = False
        report = ['rule 3:']

        ''' loop for the first edge '''
        for edge_index in self.all_edges:
            if edge_index in self.all_edges: # to make sure it is not deleted in previous runs
                edge_item = self.get_item(edge_index)

                ''' loop for the second edge '''
                for other_edge_index in self.all_edges:
                    if edge_index != other_edge_index:
                        if other_edge_index in self.all_edges and edge_index in self.all_edges: # to make sure it is not deleted in previous runs
                            other_edge_item = self.get_item(other_edge_index)

                            ''' check the intersections '''
                            intersection = intersect_line_line(
                                line_1_point_1=edge_item.pos_1,
                                line_1_point_2=edge_item.pos_2,
                                line_2_point_1=other_edge_item.pos_1,
                                line_2_point_2=other_edge_item.pos_2
                            )
                            distance_1_1 = distance_point_to_point(edge_item.pos_1, other_edge_item.pos_1)
                            distance_1_2 = distance_point_to_point(edge_item.pos_1, other_edge_item.pos_2)
                            distance_2_1 = distance_point_to_point(edge_item.pos_2, other_edge_item.pos_1)
                            distance_2_2 = distance_point_to_point(edge_item.pos_2, other_edge_item.pos_2)
                            point_to_point_distances = [distance_1_1, distance_1_2, distance_2_1, distance_2_2]
                            distance_1_2 = distance_point_to_line(edge_item.pos_1, other_edge_item.pos_1, other_edge_item.pos_2)
                            distance_2_2 = distance_point_to_line(edge_item.pos_2, other_edge_item.pos_1, other_edge_item.pos_2)
                            distance_1_1 = distance_point_to_line(other_edge_item.pos_1, edge_item.pos_1, edge_item.pos_2)
                            distance_2_1 = distance_point_to_line(other_edge_item.pos_2, edge_item.pos_1, edge_item.pos_2)
                            point_to_line_distances = [distance_1_1, distance_1_2, distance_2_1, distance_2_2]
                            if intersection is not None and \
                                min(point_to_point_distances) > self.proximity_radius and \
                                min(point_to_line_distances) > self.proximity_radius:

                                if edge_item.type == 'road' and other_edge_item.type == 'road':
                                    new_edge_item_1 = Road(pos_1=edge_item.pos_1, pos_2=intersection)
                                    new_edge_item_2 = Road(pos_1=intersection, pos_2=edge_item.pos_2)
                                    new_edge_item_3 = Road(pos_1=other_edge_item.pos_1, pos_2=intersection)
                                    new_edge_item_4 = Road(pos_1=intersection, pos_2=other_edge_item.pos_2)
                                    self.add(new_edge_item_1)
                                    report.append(str(new_edge_item_1) + ' added.')
                                    self.add(new_edge_item_2)
                                    report.append(str(new_edge_item_2) + ' added.')
                                    self.add(new_edge_item_3)
                                    report.append(str(new_edge_item_3) + ' added.')
                                    self.add(new_edge_item_4)
                                    report.append(str(new_edge_item_4) + ' added.')
                                    self.remove_item(edge_index)
                                    report.append(str(edge_item) + ' removed.')
                                    self.remove_item(other_edge_index)
                                    report.append(str(other_edge_item) + ' removed.')
                                    anything_happened = True

        return anything_happened, report
    
    def grammar_rule_4(self):
        """
        Check for edges having similar starting and ending points
        """
        anything_happened = False
        report = ['rule 3:']

        ''' loop for the first edge '''
        for edge_index in self.all_edges:
            if edge_index in self.all_edges: # to make sure it is not deleted in previous runs
                edge_item = self.get_item(edge_index)

                ''' loop for the second edge '''
                for other_edge_index in self.all_edges:
                    if edge_index != other_edge_index:
                        if other_edge_index in self.all_edges and edge_index in self.all_edges: # to make sure it is not deleted in previous runs
                            other_edge_item = self.get_item(other_edge_index)

                            ''' check the similar starting and ending points '''
                            distance_1_1 = distance_point_to_point(edge_item.pos_1, other_edge_item.pos_1)
                            distance_1_2 = distance_point_to_point(edge_item.pos_1, other_edge_item.pos_2)
                            distance_2_1 = distance_point_to_point(edge_item.pos_2, other_edge_item.pos_1)
                            distance_2_2 = distance_point_to_point(edge_item.pos_2, other_edge_item.pos_2)
                            point_to_point_distances = [distance_1_1, distance_1_2, distance_2_1, distance_2_2]
                            point_to_point_distances = sorted(point_to_point_distances)
                            distances = point_to_point_distances[:2]
                            if distances[0] < self.proximity_radius and \
                                distances[1] < self.proximity_radius:
                                self.remove_item(other_edge_index)
                                report.append(str(other_edge_item) + ' removed.')

        return anything_happened, report
