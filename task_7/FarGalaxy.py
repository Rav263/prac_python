from itertools import combinations

def count_dist(pair):
    fir, sec = pair
    return (fir[0] - sec[0]) ** 2 + (fir[1] - sec[1]) ** 2 + (fir[2] - sec[2]) ** 2

planets = []

while True:
    words = input().split()
    if len(words) == 1:
        break
    planets.append((float(words[0]), float(words[1]), float(words[2]), words[3]))

distance = 0

print(*sorted((lambda x: [x[0][3], x[1][3]])(max(combinations(planets, 2), key=count_dist))))
