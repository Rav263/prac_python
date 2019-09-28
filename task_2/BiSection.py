from math import *
import numpy as np
import readline
func_str = input()
number_str = input()

a = tuple(number_str.split(","))
for x in range(int(a[0]), int(a[1])):
    print(eval(func_str))

