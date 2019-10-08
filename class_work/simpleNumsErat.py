l = list(range(2, int(input())+ 1))

for ind in range(len(l)):
    for i in range(ind + 1, len(l)):
        if l[ind] != 0 and l[i] % l[ind] == 0:
            l[i] = 0

for i in l:
    if i != 0:
        print(i, end=" ")
print("")
