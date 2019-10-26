string = input()
patterns = input().split("@")

now_pattern  = 0
index = 0
start_index = 0

while index < len(string):
    if (now_pattern == 0):
        start_index = index
    for index_in_pat in range(len(patterns[now_pattern])):
        print(index, index_in_pat, now_pattern, string[index], patterns[now_pattern][index_in_pat])
        if string[index] != patterns[now_pattern][index_in_pat]:
            now_pattern = 0
            break
        index += 1
    else:
        now_pattern += 1
        if now_pattern == len(patterns):
            break
    
    index +=1

print(start_index)
