# Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
def is_valid_triangle(angle1, angle2, angle3):
    return "Valid triangle" if angle1 + angle2 + angle3 == 180 else "Invalid triangle"

angle1, angle2, angle3 = map(int, input("Enter three angles separated by space: ").split())
print(is_valid_triangle(angle1, angle2, angle3))