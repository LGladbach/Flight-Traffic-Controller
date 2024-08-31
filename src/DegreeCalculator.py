import math

class DegreeCalculator:
    """
    Class delivering static method to calculate degree on compass scale from a vector (Two-dimensional)
    and reverse.
    """
    @staticmethod
    def calc_degree_from_vector(vc:(float, float)):
        if vc[1] == 0:
            vc = (vc[0], 0.00000001)
        if vc[0] >= 0 and vc[1] >= 0:
            return round(math.atan(vc[0] / vc[1]) / 3.14 * 180, 0)
        elif vc[0] < 0 <= vc[1]:
            return round(360 + math.atan(vc[0] / vc[1]) / 3.14 * 180, 0)
        elif vc[0] >= 0 > vc[1]:
            return round(180 + math.atan(vc[0] / vc[1]) / 3.14 * 180, 0)
        elif vc[0] < 0 and vc[1] < 0:
            return round(180 + math.atan(vc[0] / vc[1]) / 3.14 * 180, 0)

    @staticmethod
    def calc_vector_from_degree(degree:int) -> (float, float):
        if 0 <= degree <= 90 :
            result = (1, math.tan((90 - degree) / 180 * 3.14))
        elif 90 < degree <= 180:
            result = (1, math.tan((90 - degree) / 180 * 3.14))
        elif 180 < degree <= 270:
            result = (-1, math.tan((degree - 270) / 180 * 3.14))
        elif 270 < degree <= 360:
            result = (-1, math.tan((degree - 270) / 180 * 3.14))
        #Shorten vector
        return result