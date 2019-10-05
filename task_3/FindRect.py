first_str = input()

list_of_str = []

while True:
    str = input()
    if str == first_str:
        break

    list_of_str.append(str)

list_of_sq = []
last_list_of_sq = []

counter = 0

for y in range(len(list_of_str)):
    str = list_of_str[y]

    is_rect = False
    start_coord = 0

    for index in range(len(str)):
        if str[index] == '#':
            if is_rect == False:
                start_coord = index
                is_rect = True
        else:
            if is_rect:
                is_rect = False
                list_of_sq.append((start_coord, index))
                if list_of_sq[-1] not in last_list_of_sq:
                    counter += 1;

    last_list_of_sq = list_of_sq.copy()
    list_of_sq = []
print(counter)
