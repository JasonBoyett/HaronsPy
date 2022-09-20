import tkinter as tkinter
from tkinter import simpledialog as dialog
from tkinter import messagebox as messagebox
import math
import triangle as tri

def is_vowel(character):
    if character.lower() == 'a':
        return True
    elif character.lower() == 'e':
        return True
    elif character.lower() == 'i':
        return True
    elif character.lower() == 'o':
        return True
    elif character.lower() == 'u':
        return true
    else:
        return False



side_one = float(input("please enter the length of side one: "))
side_two = float(input("please enter the length of side two: "))
side_three = float(input("please enter the length of side three: "))
my_triangle = tri.triangle(side_one,side_two,side_three)
print("that is a{insert} {type} ".format( insert = "n" if is_vowel(my_triangle.type[0])  else "", type = my_triangle.type))
if my_triangle.is_valid():
    print("its area is {0} units".format(str(my_triangle.area)))
else:
    print("there is no area")