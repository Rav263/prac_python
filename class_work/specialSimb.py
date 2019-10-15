a = list()

string = input()
strs = list()


while len(string) != 0:
    for i in a:
        for b in string:
            i.add(b)

    a.append(set())

    strs.append((set(string), string))
    string = input()

for i, b in enumerate(a):
    for j, st in enumerate(strs):
        if i == j:
            continue
print(strs)
print(a)


for i, b in enumerate(a):
    print(len(b.difference(strs[i][0])))
#print(strs[max((len(a.difference(b[0])), i) for i, b in enumerate(strs))[1]][1])

