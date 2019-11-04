planets = []

while True:
    words = input().split()
    if len(words) == 1:
        break
    planets.append((float(words[0]), float(words[1]), float(words[2]), words[3]))

first = ""
second = ""
distance = 0


for i in range(0, len(planets)):
    for j in range(i + 1, len(planets)):
        fir, sec = planets[i], planets[j]

        now_dist = (fir[0] - sec[0]) ** 2 + (fir[1] - sec[1]) ** 2 + (fir[2] - sec[2]) ** 2

        if now_dist > distance:
            distance = now_dist
            first = fir[3]
            second = sec[3]

if second > first:
    print(first, second)
else:
    print(second, first)
