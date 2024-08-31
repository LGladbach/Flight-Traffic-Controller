import math

class DegreeCalculator:
    """
    Class delivering static method to calculate degree on compass scale from a vector (Two-dimensional)
    """
    @staticmethod
    def calc_degree_from_vector(vc:(float, float)):
        if vc[0] == 0:
            vc = (0.0001, vc[1])
        if vc[0] >= 0 and vc[1] >= 0:
            return round(math.atan(vc[1] / vc[0]) / 3.14 * 180, 0)
        elif vc[0] < 0 <= vc[1]:
            return round(360 + math.atan(vc[1] / vc[0]) / 3.14 * 180, 0)
        elif vc[0] >= 0 > vc[1]:
            return round(180 + math.atan(vc[1] / vc[0]) / 3.14 * 180, 0)
        elif vc[0] < 0 and vc[1] < 0:
            return round(270 - math.atan(vc[1] / vc[0]) / 3.14 * 180, 0)