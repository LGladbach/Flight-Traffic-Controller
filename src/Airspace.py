import src.Plane
import src.Runway

class Airspace:
    """
    Implements the physical area the flight traffic controller has to control.
    Attributes:
        size (float, float) : area is represented as a rectangle
        runways list[Runway] : list of all runways in the given area
        planes list[Plane] : list of all planes in the airspace
    Functions:
        append_runway : args [new_runway:Runway] : appends new runway to runway list
        append_plane : args [new_plane:Plane] : appends new plane to plane list (happens when plane enters airspace)
    """

    def __init__(self, area_size:(float, float), runway_list=None):
        if runway_list is None:
            runway_list = []
        self._size = area_size
        self._runways = runway_list
        self._planes = []

    def append_runway(self, new_runway:src.Runway.Runway): #Add type hint, when runway class is implemented
        self._runways.append(new_runway)

    def append_plane(self, new_plane:src.Plane.Plane):
        self._planes.append(new_plane)

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