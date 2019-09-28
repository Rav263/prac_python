N = int(input())

flag = False

for i in range(2,N - 1):
    j = 1
    tmp = i**j
    while tmp <= N:
        if (tmp == N):
            flag = True
            break;
        j += 1
        tmp = i**j

if flag:
    print("YES")
else:
    print("NO")
