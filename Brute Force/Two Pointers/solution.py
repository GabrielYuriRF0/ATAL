from math import sqrt
from math import pow

def distanceOfTwoPoints(point1, point2):
    return sqrt(pow((point1[0] - point2[0]), 2) + pow((point1[1] - point2[1]), 2))


def smallerDistanceBetweenTwoPoints(points):
    pointsSize = len(points)
    smallerDistance = float('inf')
    result = [None, None]

    for i in range(0, pointsSize -1):
        for j in range(i+1, pointsSize):
            currentDistance = distanceOfTwoPoints(points[i], points[j])
            if currentDistance < smallerDistance:
                smallerDistance = currentDistance
                result[0] = points[i]
                result[1] = points[j]
    return result

points = [(36.788374396333055, 43.664220291537724),
 (62.311133419477095, 22.68131528212929),
 (72.34508182211759, 56.8597470330214),
 (76.96487063147922, 49.775584176318986),
 (5.998016242692272, 10.879626199947213),
 (81.60792171817636, 57.6261450879061),
 (2.6363604436719257, 28.418123917696203),
 (26.26265010035993, 36.330508991493325),
 (83.45483279616697, 95.1026669345308),
 (88.76865971438858, 3.3728233397428697)]

print(smallerDistanceBetweenTwoPoints(points))