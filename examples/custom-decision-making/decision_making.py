from piperabm.society.decision_making import DecisionMaking
from piperabm.society.actions.action import Move


class CustomDecisionMaking(DecisionMaking):
    """
    Methods related to agents' decision-making
    """

    def decide_destination(self, agent_id: int, duration: float) -> None:
        """
        Decide the destination
        """
        destination_id = None
        critical_stay_length = duration
        action_queue = self.get_action_queue(id=agent_id)
        # Find suitable market
        destinations = self.preasssumed_destinations(agent_id=agent_id)
        destinations = sorted(destinations, key=lambda x: x['score'], reverse=True)
        suitable_destination_found = False
        for destination in destinations:
            path = self.infrastructure.path(
                id_start=self.get_current_node(id=agent_id),
                id_end=destination['id']
            )
            move_go = Move(
                action_queue=action_queue,
                path=path,
                usage=self.transportation_degradation
            )
            # Stay (at the destination)
            stay_length = self.max_time_outside - (2 * move_go.total_duration)
            if stay_length > critical_stay_length:
                suitable_destination_found = True
                destination_id = destination['id']
                break
        if suitable_destination_found is True:
            self.go_and_comeback_and_stay(action_queue, move_go, stay_length)
        elif suitable_destination_found is False:
            destinations = self.search_destinations(agent_id=agent_id)
            destinations = sorted(destinations, key=lambda x: x['score'], reverse=True)
            for destination in destinations:
                path = self.infrastructure.path(
                    id_start=self.get_current_node(id=agent_id),
                    id_end=destination['id']
                )
                move_go = Move(
                    action_queue=action_queue,
                    path=path,
                    usage=self.transportation_degradation
                )
                # Stay (at the destination)
                stay_length = self.max_time_outside - (2 * move_go.total_duration)
                if stay_length > critical_stay_length:
                    suitable_destination_found = True
                    destination_id = destination['id']
                    break
            if suitable_destination_found is True:
                self.go_and_comeback_and_stay(action_queue, move_go, stay_length)
            elif suitable_destination_found is False:
                pass # No suitable destination found
        return destination_id
