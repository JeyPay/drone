
import math
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

# Coords du pilote
lat1 = radians(50.758995)
lon1 = radians(4.332965)
alt1 = 60

# Coords du drone
lat2 = radians(50.787592)
lon2 = radians(4.325814)
alt2 = 67

print(lat1,lon1,lat2,lon2)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c * 1000

print("Result:", distance)

alt_dif = alt2 - alt1
A2 = (distance**2) + (alt_dif**2)
A = sqrt(A2)
print('ResultAltDist:',A)

angle_cam = math.degrees(math.atan(alt_dif/distance))
print('angle_cam',angle_cam)
print('a',a)
print('c',c)

print('Le pilote est au : ',end='')
north_south = (lat2 - lat1) * 1000
if north_south < 0:
    print('Nord',end=' - ')
elif north_south > 0:
    print('Sud',end=' - ')
else:
    print('Null',end=' - ')

west_east = (lon2 - lon1) * 1000
if west_east < 0:
    print('Est')
elif west_east > 0:
    print('Ouest')
else:
    print('Null')

print('Et en voici les valeurs : ',north_south," ",west_east)
val1 = (north_south-west_east)/(50000/45)
val2 = (west_east-north_south)/(5000/45)
print(val1)
print(val2)



    

