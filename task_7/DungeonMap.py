from collections import defaultdict

dictionary = defaultdict(list)

while True:
    words = input().split()
    
    if len(words) == 1:
        start = words[0]
        end = input()
        break
    
    dictionary[words[0]].append(words[1])
    dictionary[words[1]].append(words[0])


was_there = set()
stack = [start]

while stack:
    now = stack.pop()
    was_there.add(now)

    for some in dictionary[now]:
        if some not in was_there:
            stack.append(some)


if end in was_there:
    print("YES")
else:
    print("NO")

