# Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter.
def compare_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return "Area is greater" if area > perimeter else "Perimeter is greater"

length, breadth = map(int, input("Enter length and breadth separated by space: ").split())
print(compare_area_perimeter(length, breadth))