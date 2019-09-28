pal = int(input())

tmp_pal = pal
second_pal = 0

while pal >= 1:
    second_pal *= 10
    second_pal += int(pal % 10)

    pal = int(pal / 10)

if tmp_pal == second_pal:
    print("YES")
else:
    print("NO")
