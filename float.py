""" Show the concept of floating point imprecision """
from cs50 import get_float

x = get_float("x: ")
y = get_float("y: ")

z = x/y

print(f"x / y = {z:.50f}")