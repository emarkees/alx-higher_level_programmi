#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
  print("0: is positive")
elif number == 0:
  print("0: is zero")
else:
  print("0: is negative")
