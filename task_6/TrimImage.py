    
rects = []
field = [0, 0, 0, 0]
first = True

while True:
    x, y, w, h, ch = input().split()
    x, y, w, h = int(x), int(y), int(w), int(h)

    if x == 0 and y == 0 and w == 0 and h == 0:
        break
    
    if w == 0 or h == 0:
        continue

    if first:
        field[0] = min(x + w, x);
        field[1] = max(x + w, x);
        field[2] = min(y + h, y);
        field[3] = max(y + h, y);
    first = False

    field[0] = min(x + w, x, field[0]);
    field[1] = max(x + w, x, field[1]);
    field[2] = min(y + h, y, field[2]);
    field[3] = max(y + h, y, field[3]);

    rects.append((x, y, w, h, ch))

image_weight = field[1] - field[0]
image_height = field[3] - field[2]

processed_rects = []

image = []

for i in range(image_height):
    image.append(['.'] * image_weight)


for rect in rects:
    x = rect[0] - field[0] + (rect[2] if rect[2] < 0 else 0)
    y = rect[1] - field[2] + (rect[3] if rect[3] < 0 else 0)

    processed_rects.append((x, y, abs(rect[2]), abs(rect[3]), rect[4]))

for rect in processed_rects:
    for y in range(rect[1], rect[3] + rect[1]):
        for x in range(rect[0], rect[2] + rect[0]):
            image[y][x] = rect[4]

for line in image:
    print(*line, sep='')
