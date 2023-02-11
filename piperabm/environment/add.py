from piperabm.boundary import Point
from piperabm.unit import Date
from piperabm.tools import euclidean_distance
from piperabm.degradation import Eternal


class Add:

    def add_settlement(
        self,
        name='',
        pos=[0, 0],
        boundary=Point(),
        active=True,
        initiation_date=Date.today(),
        degradation_dist=Eternal()
    ):
        """
        Add a new settlement
            name: name of the settlement, optional
            pos: position of the settlement, [x, y]
            boundary: shape of the settlement
            active: is it cuurently active? (True/False)
            initiation_date: the built date of the settlement
            degradation_dist: the distribution for degradation of the settlement
        """
        create_node = True
        if self.find_node(pos, report=False) is not None:
            create_node = False
        if self.find_node(name, report=False) is not None:
            create_node = False

        if create_node is True:
            index = self.find_next_index()
            boundary.center = pos
            self.G.add_node(
                index,
                name=name,
                active=active,
                initiation_date=initiation_date,
                degradation_dist=degradation_dist,
                boundary=boundary
            )
            self.node_types['settlement'].append(index)
        else:
            print('duplicate node data, settlement node not created')

    def add_cross(
        self,
        name='',
        pos=[0, 0]
    ):
        """
        Add a new cross point
            name: name of the cross point, optional
            pos: position of the settlement, [x, y]
        """
        create_node = True
        if self.find_node(pos, report=False) is not None:
            create_node = False
        if self.find_node(name, report=False) is not None:
            create_node = False

        if create_node is True:
            index = self.find_next_index()
            boundary = Point()
            boundary.center = pos
            self.G.add_node(
                index,
                name=name,
                boundary=boundary
            )
            self.node_types['cross'].append(index)
            return index
        else:
            print('duplicate node data, cross node not created')
            return None

    def add_market(
        self,
        name='',
        pos=[0, 0],
        boundary=Point(),
        active=True,
        initiation_date=Date.today(),
        degradation_dist=Eternal()
    ):
        """
        Add a new market
            name: name of the market, optional
            pos: position of the market, [x, y]
            boundary: shape of the market
            active: is it cuurently active? (True/False)
            initiation_date: the built date of the market
            degradation_dist: the distribution for degradation of the market
        """
        create_node = True
        if self.find_node(pos, report=False) is not None:
            create_node = False
        if self.find_node(name, report=False) is not None:
            create_node = False

        if create_node is True:
            index = self.find_next_index()
            boundary.center = pos
            self.G.add_node(
                index,
                name=name,
                active=active,
                initiation_date=initiation_date,
                degradation_dist=degradation_dist,
                boundary=boundary
            )
            self.node_types['market'].append(index)
        else:
            print('duplicate node data, market node not created')

    def add_link(
        self,
        start,
        end,
        active=True,
        initiation_date=Date.today(),
        degradation_dist=Eternal(),
        total_axels=100, ###
        current_axels=0,
        length=None,
        difficulty=1
    ):
        """
        Add a link between *start* and *end*

        Args:
            start: starting point in the form of either index (as int), name (as str), or pos (as a [x,y] list)
            end: ending point in the form of either index (as int), name (as str), or pos (as a [x,y] list)
            active: is it still active? (True/False)
            initiation_date: the built date of settlement
            degradation_dist: the distribution for degradation of the settlement
            length: the length of the link, eucledian distance is used as default
            difficulty: difficulty of the link (unrelated to slope), default is 1
        """
        create_node = True
        start_index = self.find_node(start, report=False)
        if start_index is None:
            if isinstance(start, list):
                start_index = self.add_cross(pos=start)
            else:
                create_node = False
        end_index = self.find_node(end, report=False)
        if end_index is None:
            if isinstance(end, list):
                end_index = self.add_cross(pos=end)
            else:
                create_node = False

        if create_node is True:
            start_pos = self.G.nodes[start_index]['boundary'].center
            end_pos = self.G.nodes[end_index]['boundary'].center
            euclidean_length = euclidean_distance(*start_pos, *end_pos)
            if length is None or length < euclidean_length:
                length = euclidean_length  # default value
            #progressive_degradation_factor=self.progressive_degradation_factor(current_axels, total_axels)

            self.G.add_edge(
                start_index,
                end_index,
                active=active,
                initiation_date=initiation_date,
                degradation_dist=degradation_dist,
                total_axels=total_axels,
                current_axels=current_axels,
                length=length,
                difficulty=difficulty
            )
        else:
            print('link creation failed.')
