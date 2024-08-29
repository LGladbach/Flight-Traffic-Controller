class Plane:
    """
    Implements planes in the Airspace the flight controller controls.
    Class Internal attributes:
        last_id int : Highest id given to a plane, initially -1.
    Attributes:
        id int : Identification number of the plane (automatically defined by class)
        position (int, int) : Position in airspace
        prev_position (int, int) : Previous position (changes with every change of position)
        speed (int, int) : Two-dimensional derivation of position

    """

    last_id = -1

    def __init__(self, init_position:(int, int), init_speed:(int, int)):
        self._id = Plane.last_id + 1
        Plane.last_id += 1 #Autoincrement id of planes (currently not Thread safe)
        self._position = init_position
        self._prev_position = (0, 0)
        self._speed = init_speed

    def calc_speed(self):
        """
        Calculates the speed of the plane dependent on current and previous position.
        return None
        """
        self.speed = (self._position[0] - self._prev_position[0], self._position[1] - self._prev_position[1])

    @property
    def id(self):
        return self._id

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position:(int, int)):
        self._position, self._prev_position = new_position, self._position
        self.calc_speed()

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed: (int, int)):
        self._speed = new_speed