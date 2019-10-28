string = input()
pattern = input()

index = 0
start_index = 0

while index < len(string):
    start_index = index
    index_in_pat = 0
    while index_in_pat < len(pattern):
        if index >= len(string):
            break
        flg = False
#        print(index, index_in_pat, string[index], pattern[index_in_pat])
        while pattern[index_in_pat] == "@":
            flg = True
            index_in_pat += 1
            index += 1
            if index_in_pat >= len(pattern):
                flg = False
                break
            if index >= len(string):
                break
        else:
            #print("INDEX=", index)
            if string[index] != pattern[index_in_pat]:
                index = start_index
                index_in_pat = 0
                break
            flg = False

        if flg:
            break
        index += 1
        index_in_pat += 1
    else:
        print(start_index)
        break
    index +=1
else:
    print(-1)
