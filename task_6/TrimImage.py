rects = []
field = [0, 0, 0, 0]

while True:
    x, y, h, w, ch = input().split()
    x, y, w, h = int(x), int(y), int(w), int(h)

    if x == 0 and y == 0 and w == 0 and h == 0:
        break
    
    if x + w < field[0]:
        field[0] = x + w
    if x + w > field[1]:
        field[1] = x + w
    if y + h < field[2]:
        field[2] = y + h
    if y + h > field[3]:
        field[3] = y + h

    rects.append((x, y, w, h, ch))

image_weight = field[1] - field[0]
image_height = field[3] - field[2]

processed_rects = []

for rect in rects:
    x = rect[0] + image_weight//2 if field[0] < 0 else 0
    y = rect[1] + image_weight//2 if field[2] < 0 else 0

    if rect[2] < 0:
        x -= rect[2]
    if rect[3] < 0:
        y -= rect[3]

    processed_rects.append((x, y, abs(rect[2]), abs(rect[3]), rect[4]))

print(processed_rects)
for y in range(image_height):
    for x in range(image_weight):
        pr_ch = '.'
        for rect in processed_rects:
            if x >= rect[0] and x <= rect[2] + x and y >= rect[1] and y <= rect[3] + y:
                pr_ch = rect[4]
        print(pr_ch , end="")
    print()

print(rects, field)
