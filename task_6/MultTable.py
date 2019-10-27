from math import ceil
n, size = eval(input())

max_len = len(str(n * n))
num_len = len(str(n))

split_str = "=" * size;
string_len = max_len + num_len * 2 + 9
string_len = (size + 3) // string_len
rows = ceil(n / string_len)


print(split_str)
strings = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        string = f"{i:>{num_len}} * {j:<{num_len}} = {i*j:<{max_len}} "
        strings.append(string)
for s in range(rows):
    for a in range(n):
        for b in range(string_len):
            if s * n * string_len + b * n + a >= len(strings):
                continue
            if b != 0: print("| ", end="")
            print(strings[s * n * string_len + b * n + a], end="")
        print()
    print(split_str)
