# 1) Write a definition for a class named Circle with 
# attributes center and radius,
#where center is a Point (x, y) tuple and radius is a number
class Circle:
    def __init__(self, center=(0,0), radius=1):
        self.center = center
        self.radius = radius

# 2) Instantiate a Circle object that represents a circle with
# its center at (150, 100) and radius 75
# default_circ = Circle

circ = Circle(center=(150,100), radius=75)

print(f"The center of the circle is {circ.center} and the radius is {circ.radius}.")


# 3) Write a function named point_in_circle that takes a
# Circle and a Point and returns True if the
# Point lies in or on the boundary of the circle.
# DOCS: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
def point_in_circle(circle, point):
    x_center, y_center = circle.center
    x, y = point
    return (x- x_center)**2 + (y-y_center)**2 < circle.radius**2

print(point_in_circle(circ,(100,100)))
    
