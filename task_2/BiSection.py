from math import *

func_str = input()
number_str = input()

a = tuple(number_str.split(","))
start, end = float(a[0]), float(a[1])

func = eval("lambda x: " + func_str);

mid = (end + start) / 2
eps = 0.000001

while abs(func(mid)) > eps:
    if func(start) * func(mid) < 0:
        end = mid
    else:
        start = mid
    mid = (end + start) / 2

print(mid)
