import tkinter as tkinter
from tkinter import simpledialog as dialog
from tkinter import messagebox as messagebox
import math

class triangle:
    def is_valid(self):
        if self.area <= 0:
            return False
        if math.isnan(self.area):
            return False
        else:
            return True

    def get_triangle_type(self):
        if self.side_one == self.side_two and self.side_two == self.side_three:
            return "Equilateral triangle"
        if ((self.side_one ** 2 + self.side_two ** 2) == self.side_three ** 2) or ((self.side_one ** 2 + self.side_three ** 2) == self.side_two **2) or((self.side_two ** 2 + self.side_three ** 2) == self.side_one ** 2) :                
            return "Right triangle"
        if not self.is_valid():
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

def is_vowel(character):
    if character.lower() == 'a':
        return True
    if character.lower() == 'e':
        return True
    if character.lower() == 'i':
        return True
    if character.lower() == 'o':
        return True
    if character.lower() == 'u':
        return true
    else:
        return False


side_one = float(input("please enter the length of side one: "))
side_two = float(input("please enter the length of side two: "))
side_three = float(input("please enter the length of side three: "))
my_triangle = triangle(side_one,side_two,side_three)
print("that is a{insert} {type} ".format( insert = "n" if is_vowel(my_triangle.type[0])  else "", type = my_triangle.type))
if my_triangle.is_valid():
    print("its area is {0} units".format(str(my_triangle.area)))
else:
    print("there is no area")