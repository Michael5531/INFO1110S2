class Circle():
    def __init__(self, pi, radius):
        pi = 3.1415
        self.pi = pi
        self.radius = radius
    def get_area(self):
        area = pi * self.radius ** 2
        return area
pi = 3.1415
c1 = Circle(pi, 2)
c1_area = c1.get_area()

# c2 = Circle(pi, 5)
# c2_area = c2.get_area(pi, 5)

# c3 = Circle(pi, 4)
# c3_area = c3.get_area(pi, 4)

print("Circle 1 area is: {:.2f}".format(c1_area))
# print("Circle 2 area is: {:.2f}".format(c2_area))
# print("Circle 3 area is: {:.2f}".format(c3_area))
