def turtle(coord, direction):
    change_dir = True
    while True:
        if not change_dir:
            if direction == 0:
                coord = (coord[0] + 1, coord[1])
            elif direction == 1:
                coord = (coord[0], coord[1] + 1)
            elif direction == 2:
                coord = (coord[0] - 1, coord[1])
            elif direction == 3:
                coord = (coord[0], coord[1] - 1)

        command = yield coord
        if command == "f":
            change_dir = False
        elif command == "l":
            direction += 1
            direction %= 4
            change_dir = True
        elif command == "r":
            direction -= 1
            direction = direction if direction >= 0 else 3
            change_dir = True

