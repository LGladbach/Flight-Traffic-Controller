from src.DegreeCalculator import DegreeCalculator

class Plane:
    """
    Implements planes in the Airspace the flight controller controls.
    Class Internal attributes:
        last_id int : Highest id given to a plane, initially -1.
    Attributes:
        id int : Identification number of the plane (automatically defined by class)
        position (float, float) : Position in airspace
        prev_position (float, float) : Previous position (changes with every change of position)
        speed float : Absolute value of position change
        direction int : direction in degrees (0° is north)
    Functions:
        calc_speed : update the speed vector on position change
    """

    last_id = -1

    def __init__(self, init_position:(float, float), init_speed:float, init_direction:int) -> None:
        self._id = Plane.last_id + 1
        Plane.last_id += 1 #Autoincrement id of planes (currently not Thread safe)
        self._position = init_position
        self._prev_position = (0, 0)
        self._speed = init_speed
        self._direction = init_direction

    def calc_speed_and_direction(self) -> None:
        """
        Calculates the speed of the plane dependent on current and previous position.
        return None
        """
        change_vector = (self._position[0] - self._prev_position[0], self._position[1] - self._prev_position[1])
        self._speed = (change_vector[0]**2 + change_vector[1]**2)**0.5
        self._direction = DegreeCalculator.calc_degree_from_vector(change_vector)

    @property
    def id(self) -> int:
        return self._id

    @property
    def position(self) -> (float, float):
        return self._position

    @position.setter
    def position(self, new_position:(float, float)) -> None:
        self._position, self._prev_position = new_position, self._position
        self.calc_speed_and_direction()

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def direction(self) -> int:
        return self._direction