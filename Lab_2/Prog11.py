# Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.
def are_points_collinear(x1, y1, x2, y2, x3, y3):
    return "Points are collinear" if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1) else "Points are not collinear"

x1, y1 = map(int, input("Enter coordinates of point 1 (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates of point 2 (x2 y2): ").split())
x3, y3 = map(int, input("Enter coordinates of point 3 (x3 y3): ").split())
print(are_points_collinear(x1, y1, x2, y2, x3, y3))