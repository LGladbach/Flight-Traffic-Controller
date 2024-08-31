import src.Plane
import src.Runway

class Airspace:
    """
    Implements the physical area the flight traffic controller has to control.
    Attributes:
        size (int, int) : area is represented as a rectangle
        runways list[Runway] : list of all runways in the given area
        planes list[Plane] : list of all planes in the airspace
        rule_set list[Rule] : list of rules the flight traffic controller has to comply with
    Functions:
        append_runway : args [new_runway:Runway] : appends new runway to runway list
        append_plane : args [new_plane:Plane] : appends new plane to plane list (happens when plane enters airspace)
        append_rule : args [new_rule:Rule] : appends new rule to rule_set list
    """

    def __init__(self, area_size:(int, int), runway_list=None, rules=None):
        if runway_list is None:
            runway_list = []
        if rules is None:
            rules = []
        self._size = area_size
        self._runways = runway_list
        self._planes = []
        self._rule_set = rules

    def append_runway(self, new_runway:src.Runway.Runway): #Add type hint, when runway class is implemented
        self._runways.append(new_runway)

    def append_plane(self, new_plane:src.Plane.Plane):
        self._planes.append(new_plane)

    def append_rule(self, new_rule): #Add type hint, when rule class is implemented
        self._rule_set.append(new_rule)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size:(int, int)):
        self._size = new_size

    @property
    def runways(self):
        return self._runways

    @property
    def planes(self):
        return self._planes

    @property
    def rule_set(self):
        return self._rule_set