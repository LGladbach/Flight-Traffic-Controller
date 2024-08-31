import src.Airspace

class TrafficController:
    """
    Implements the traffic control algorithm. (So far only for one runway, some very simple planes)
    Attributes:
        airspace Airspace : Airspace controlled by the Controller
        rule_set list[Rule] : list of rules the flight traffic controller has to comply with
        precalc_air_situation List[List[Plane Positions for time step]]: Calculation of flight-paths in the future
        standard_routes list[Route] : stores Routes for planes to wait, approach, take off, etc.
    Functions:
        append_rule : args [new_rule:Rule] : appends new rule to rule_set list
        create_waiting_loop : args [approach_route: Route, min_distance_to_runway: float] : tries to find a route in airspace where planes can safely wait on approach
    """
    def __init__(self, init_airspace:src.Airspace.Airspace, rules=None) -> None:
        self._airspace = init_airspace
        if rules is None:
            rules = []
        self._rule_set = rules
        self._precalc_air_situation = []

    def append_rule(self, new_rule) -> None: #Add type hint, when rule class is implemented
        self._rule_set.append(new_rule)

    def create_waiting_loop(self, approach_route, min_distance_to_runway) -> bool:
        """
        :return: success or not (bool)
        """
        pass

    @property
    def airspace(self) -> src.Airspace.Airspace:
        return self._airspace

    @airspace.setter
    def airspace(self, new_airspace:src.Airspace.Airspace) -> None:
        pass

    @property
    def rule_set(self):
        return self._rule_set

    @property
    def precalc_air_situation(self):
        return self._precalc_air_situation