import src.DegreeCalculator
from src.DegreeCalculator import DegreeCalculator


class Runway:
    """
    Implements runways in airspace.
    Attributes:
        end1, end2 (float, float) : end points of the runway (runway is represented as a straight line)
        length float : length of the runway
        approach_vectors ((float, float), (float, float)) : vectors of the approach direction
        approach_degrees (int, int) : Conversion of approach vectors to degrees on compass scale
    """

    def __init__(self, end1_init:(float, float), end2_init:(float, float)):
        self._end1 = end1_init
        self._end2 = end2_init
        self._approach_vectors = ((self._end1[0] - self._end2[0], self._end1[1] - self._end2[1]), (self._end2[0] - self._end1[0], self._end2[1] - self._end1[1]))
        self._length = (self._approach_vectors[0][0]**2 + self._approach_vectors[0][1]**2) ** 0.5
        self._approach_degrees = (DegreeCalculator.calc_degree_from_vector(self.approach_vectors[0]), DegreeCalculator.calc_degree_from_vector(self.approach_vectors[1]))

    @property
    def end1(self):
        return self._end1

    @property
    def end2(self):
        return self._end2

    @property
    def approach_vectors(self):
        return self._approach_vectors

    @property
    def length(self):
        return self._length

    @property
    def approach_degrees(self):
        return self._approach_degrees