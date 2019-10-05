num = int(input())
max_num = num
current_sum = 0
best_sum = 0

while num != 0:
    current_sum = max(0, current_sum + num)
    best_sum = max(best_sum, current_sum)
    if num > max_num:
        max_num = num

    num = int(input())

if best_sum == 0:
    print(max_num)
else:
    print(best_sum)
