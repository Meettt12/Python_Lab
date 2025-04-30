# Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle.
import math

def point_circle_relation(cx, cy, r, px, py):
    distance = math.sqrt(pow(px - cx, 2) + pow(py - cy, 2))
    if distance < r:
        return "Point is inside the circle"
    elif distance == r:
        return "Point is on the circle"
    else:
        return "Point is outside the circle"

cx, cy = map(int, input("Enter center of the circle (cx cy): ").split())
r = int(input("Enter radius of the circle: "))
px, py = map(int, input("Enter coordinates of the point (px py): ").split())
print(point_circle_relation(cx, cy, r, px, py))