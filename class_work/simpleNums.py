N = int(input())

counter = 0
i = 2

while counter < N:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        counter += 1
    i += 1
