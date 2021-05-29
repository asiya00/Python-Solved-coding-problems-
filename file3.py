from math import sqrt

class Coordinate:
    x = 0
    y = 0

def area_of_triangle(p1,p2,p3):
    side = lambda a, b : sqrt((b.x-a.x)**2  + (b.y-a.y)**2)
    side_one = side(p1,p2)
    side_two = side(p2,p3)
    side_three = side(p3,p1)
    s = (side_one + side_two + side_three)/2
    area = sqrt(s*(s-side_one)*(s-side_two)*(s-side_three))
    return round(area,2)

points = list() # Generate a list for Coordinate objects

for num in range(3):
    points.append(Coordinate()) # Create a new Coordinate object and append it to the list
    # Set Coordinate parameters
    points[num].x = float(input(f"Enter x coordinate of the #{num+1} point of a triangle: "))
    points[num].y = float(input(f"Enter y coordinate of the #{num+1} point of a triangle: "))

print("Area of triangle:",area_of_triangle(points[0],points[1],points[2]))