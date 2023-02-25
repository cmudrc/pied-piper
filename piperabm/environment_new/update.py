from piperabm.degradation import Eternal, DiracDelta


class Update:

    def _update_all_edges(self, start_date, end_date):
        """
        Check all edges to see whether they are active in the duration of time or not
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """
        for start, end, data in self.G.edges(data=True):
            if data['active'] is True:
                distribution = data['degradation_dist']
                length = data['length']
                if self.links_unit_length is None:
                    coeff = 1
                else:
                    if isinstance(distribution, (Eternal, DiracDelta)):
                        coeff = 1
                    else:
                        coeff = length / self.links_unit_length
                initiation_date = data['initiation_date']
                if initiation_date < end_date:
                    if initiation_date > start_date:
                        kwargs = {
                            'initiation_date': initiation_date,
                            'distribution': distribution,
                            'start_date': initiation_date,
                            'end_date': end_date,
                            'coeff': coeff,
                        }
                    else:
                        kwargs = {
                            'initiation_date': initiation_date,
                            'distribution': distribution,
                            'start_date': start_date,
                            'end_date': end_date,
                            'coeff': coeff,
                        }
                    active = self.is_active(**kwargs)
                else:
                    active = True

                if active is False:
                    data['active'] = False
                    txt = str(start_date.strftime('%Y-%m-%d')) + \
                        ' -> ' + str(end_date.strftime('%Y-%m-%d'))
                    txt += ': link ' + str(start) + '-' + \
                        str(end) + ' degradaded.'
                    self.log.add(txt)

    def _update_all_nodes(self, start_date, end_date):
        """
        Check all nodes to see whether they are active in the duration of time or not
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """
        for index in self.G.nodes():
            if index in self.node_types['settlement'] or index in self.node_types['market']:
                node = self.G.nodes[index]
                distribution = node['degradation_dist']
                initiation_date = node['initiation_date']
                if initiation_date < end_date:
                    if initiation_date > start_date:
                        kwargs = {
                            'initiation_date': initiation_date,
                            'distribution': distribution,
                            'start_date': initiation_date,
                            'end_date': end_date,
                        }
                    else:
                        kwargs = {
                            'initiation_date': initiation_date,
                            'distribution': distribution,
                            'start_date': start_date,
                            'end_date': end_date,
                        }
                    active = self.is_active(**kwargs)
                else:
                    active = True

                if active is False:
                    node['active'] = False
                    txt = str(start_date.strftime('%Y-%m-%d')) + \
                        ' -> ' + str(end_date.strftime('%Y-%m-%d'))
                    txt += ': node ' + str(index) + ' degradaded.'
                    self.log.add(txt)

    def update_elements(self, start_date, end_date):
        """
        Update all elements during the *start_date* until *end_date*
        """
        self._update_all_edges(start_date, end_date)
        self._update_all_nodes(start_date, end_date)
