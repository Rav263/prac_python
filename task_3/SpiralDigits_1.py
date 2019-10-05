N, M = input().split(",")
N, M = int(N), int(M)

b = [[-1] * N for i in range(M)]
dirr = 0
x,y = 0,0

for counter in range(M*N):
    b[y][x] = counter % 10

    if   (x == N - 1 or b[y][x + 1] != -1) and dirr == 0:
        dirr += 1
    
    elif (y == M - 1 or b[y + 1][x] != -1) and dirr == 1:
        dirr += 1
    
    elif (y == 0     or b[y - 1][x] != -1) and dirr == 3:
        dirr += 1
    
    elif (x == 0     or b[y][x - 1] != -1) and dirr == 2:
        dirr += 1
    
    dirr = dirr % 4

    if dirr == 0:
        x += 1
    elif dirr == 1:
        y += 1
    elif dirr == 2:
        x -= 1
    elif dirr == 3:
        y -= 1

for line in b:
    print(*line)
