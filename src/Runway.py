class Runway:
    """
    Implements runways in airspace.
    Attributes:
        end1, end2 (int, int) : end points of the runway (runway is represented as a straight line)
        length float : length of the runway
        approach_vectors ((int, int), (int, int)) : vectors of the approach direction
    """

    def __init__(self, end1_init:(int, int), end2_init:(int, int)):
        self._end1 = end1_init
        self._end2 = end2_init
        self._approach_vectors = ((self._end1[0] - self._end2[0], self._end1[1] - self._end2[1]), (self._end2[0] - self._end1[0], self._end2[1] - self._end1[1]))
        self._length = (self._approach_vectors[0][0]**2 + self._approach_vectors[0][1]**2) ** 0.5

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