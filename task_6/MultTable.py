n, size = eval(input())

max_len = len(str(n * n))
num_len = len(str(n))

split_str = "=" * size;
string_len = max_len + num_len * 2 + 8
string_len = (size + 1) // string_len

print(string_len)

print(split_str)
strings = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        string = f"{i:>{num_len}} * {j:<{num_len}} = {i*j:<{max_len}} "
        strings.append(string)
for s in range(n // string_len + 1):
    for a in range(n):
        for b in range(string_len):
            if s * n * string_len + b * n + a >= len(strings):
                print()
                continue
            if b != string_len - 1:
                print(strings[s * n * string_len + b * n + a], end="|")
            else:
                print(strings[s * n * string_len + b * n + a])
    print(split_str)
