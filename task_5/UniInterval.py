tuples = eval(input())

a = list((L, True) for L, R in tuples)
a += list((R, False) for L, R in tuples)

a.sort()

counter = 0
result = 0

for i, now in enumerate(a):
    result += a[i][0] - a[i-1][0] if i > 0 and counter > 0 else 0
    counter += 1 if now[1] else -1

print(result)
