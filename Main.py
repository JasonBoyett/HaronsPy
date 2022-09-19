from tkinter.simpledialog import SimpleDialog
import math

class triangle:
    def __init__(self, side_one, side_two, side_three):
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self.semi_perimeter = (side_three + side_two + side_one) / 2
        self.area = math.sqrt(self.semi_perimeter * (self.semi_perimeter - self.side_one) * (self.semi_perimeter - self.side_two) * (self.semi_perimeter - self.side_three))
    
print("please enter the lengths of each side of the triangle")
side_one = float(input("side one: "))
side_two = float(input("side two: "))
side_three = float(input("side three: "))
my_triangle = triangle(side_one,side_two,side_three)
print(my_triangle.area)