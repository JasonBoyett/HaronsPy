import math
class triangle:
    def is_valid(self):
        if self.area <= 0:
            return False
        elif math.isnan(self.area):
            return False
        else:
            return True

    def get_triangle_type(self):
        if self.side_one == self.side_two and self.side_two == self.side_three:
            return "Equilateral triangle"
        elif ((self.side_one ** 2 + self.side_two ** 2) == self.side_three ** 2) or ((self.side_one ** 2 + self.side_three ** 2) == self.side_two **2) or((self.side_two ** 2 + self.side_three ** 2) == self.side_one ** 2) :                
            return "Right triangle"
        elif not self.is_valid():
            return "Invalid triangle"
        else:
            return "Triangle"

    def define_area(self):
        try:
           return math.sqrt(self.semi_perimeter * (self.semi_perimeter - self.side_one) * (self.semi_perimeter - self.side_two) * (self.semi_perimeter - self.side_three))
        except ValueError:
            return math.nan


    
    def __init__(self, side_one, side_two, side_three):
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self.semi_perimeter = (side_three + side_two + side_one) / 2
        self.area = self.define_area()
        self.type = self.get_triangle_type()