from src.Airspace import Airspace
from src.Runway import Runway
from src.Plane import Plane

print(Runway((5, 5), (10, 10)).approach_degrees)

#Test Runways
rws = [Runway((10, 10), (15, 15))]

#Test Planes
pls = [Plane((0, 0), 0.0, 0)]

#Test Airspace
ap = Airspace((20, 20))