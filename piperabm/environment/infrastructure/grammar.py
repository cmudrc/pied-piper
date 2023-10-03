from piperabm.tools.coordinate.distance import distance_point_to_point, distance_point_to_line


class Grammar:

    def apply_grammars(self):
        """
        Apply all grammars based on a decision tree
        if a rule is not yielding any change, it is ok to go the next rule
        if not, all grammars rules start over
        """

        anything_happened = None
        while anything_happened is True or anything_happened is None:

            ''' rule 1 '''
            anything_happened = self.grammar_rule_1()
            if anything_happened is True: # start over
                self.apply_grammars()
            elif anything_happened is False: # next rule
                
                ''' rule 2 '''
                anything_happened = self.grammar_rule_2()
                if anything_happened is True: # start over
                    self.apply_grammars()
                elif anything_happened is False: # next rule
                    
                    ''' rule 3 '''
                    anything_happened = self.grammar_rule_3()
                    if anything_happened is True: # start over
                        self.apply_grammars()
                    elif anything_happened is False: # next rule
                        
                        ''' finish '''
                        break
        
    def grammar_rule_1(self):
        """
        Check for node to node proximity
        """

        anything_happened = False

        ''' loop for the first node '''
        nodes = self.all_nodes()
        for node_index in nodes:
            if node_index in self.all_nodes(): # to make sure it is not deleted in previous runs
                item = self.get_node_item(node_index)

                ''' loop for the second node '''
                for other_node_index in nodes:
                    if other_node_index in self.all_nodes(): # to make sure it is not deleted in previous runs
                        if node_index != other_node_index:
                            other_item = self.get_node_item(other_node_index)

                            ''' check the distance '''
                            distance = distance_point_to_point(item.pos, other_item.pos)
                            if distance < self.proximity_radius:
                                ''' update the nodes based on their types '''

                                if item.type == 'junction' and other_item.type != 'junction':
                                    self.replace_node(
                                        old_index=item.index,
                                        new_index=other_item.index
                                    )
                                    anything_happened = True

                                elif item.type == 'junction' and other_item.type == 'junction':
                                    self.replace_node(
                                        old_index=other_item.index,
                                        new_index=item.index
                                    )
                                    anything_happened = True

                                elif item.type != 'junction' and other_item.type == 'juction':
                                    self.replace_node(
                                        old_index=other_item.index,
                                        new_index=item.index
                                    )
                                    anything_happened = True

                                elif item.type != 'junction' and other_item.type != 'juction':
                                    pass

        return anything_happened

    def grammar_rule_2(self):
        """
        Check for node to edge proximity
        """

        anything_happened = False

        ''' loop for the node '''
        nodes = self.all_nodes()
        for node_index in nodes:
            if node_index in self.all_nodes(): # to make sure it is not deleted in previous runs
                node_item = self.get_node_item(node_index)

                ''' loop for the edge '''
                edges = self.all_edges()
                for edge_indexes in edges:
                    if edge_indexes in self.all_edges(): # to make sure it is not deleted in previous runs
                        edge_item = self.get_edge_item(*edge_indexes)

                        ''' check the distance '''
                        distance = distance_point_to_line(node_item.pos, edge_item.pos_1, edge_item.pos_2)
                        if distance is not None:
                            if distance < self.proximity_radius:
                                ''' update the items '''
                                pass

        return anything_happened

    def grammar_rule_3(self):
        """
        Check for edge to edge intersection
        """
        anything_happened = False
        return anything_happened