from collections import deque

tupe = eval(input())

d = deque()


for obj in tupe:
    if obj.__class__() is tuple():
        for min_obj in obj:
            d.append(min_obj)
    else:
        if obj > len(d):
            break
        t = []
        for inex in range(obj):
            t.append(d.popleft())
        print(tuple(t))

