#
cube = [
    list('x.+.+.+.x'),
    list('/......./+'),
    list('/......./.+'),
    list('x.+.+.+.x..+'),
    list('+.......+..x'),
    list('+.......+./'),
    list('+.......+/'),
    list('x.+.+.+.x'),
]

left_up_points = [
    [(3, 6), (3, 14), (3, 22)],
    [(6, 3), (6, 11), (6, 19)],
    [(9, 0), (9, 8), (9, 16)],
]


def start_of_rows(left_up_point):
    shifts = (
        (-3, 3), (-2, 2), (-1, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0))
    row, col = left_up_point
    result = []
    for row_delta, col_delta in shifts:
        result.append((row + row_delta, col + col_delta))
    return result


def add_cube(output, start_of_rows):
    for ind, (row, col) in enumerate(start_of_rows):
        output[row][col:col + len(cube[ind])] = cube[ind]
    return output


def to_txt(output):
    return '\n'.join(''.join(row) for row in output).replace('.', ' ')


def move_one_layer_down(output):
    return [[' '] * 34 for _ in range(4)] + output


def subtract_one(input):
    for row in range(3):
        for col in range(3):
            if input[row][col] > 0:
                input[row][col] -= 1
    stop = all(all(each <= 0 for each in row) for row in input)
    return stop, input


def left_up_points_negative(height):
    return [
        [(height - 6, 6), (height - 6, 14), (height - 6, 22)],
        [(height - 3, 3), (height - 3, 11), (height - 3, 19)],
        [(height, 0), (height, 8), (height, 16)],
    ]


def add_one(input):
    for row in range(3):
        for col in range(3):
            if input[row][col] < 0:
                input[row][col] += 1
    stop = all(all(each >= 0 for each in row) for row in input)
    return stop, input


def add_cube_bottom(output, start_of_rows):
    for ind, (row, col) in enumerate(start_of_rows):
        if row >= len(output):
            output += [[' '] * 34 for _ in range(4)]
        for i in range(len(cube[ind])):
            if output[row][col + i] == ' ':
                output[row][col + i] = cube[ind][i]
    return output


def main(input):
    output = [[' '] * 34 for _ in range(14)]

    while True:
        for row in range(3):
            for col in range(3):
                if input[row][col] > 0:
                    output = add_cube(
                        output,
                        start_of_rows(left_up_points[row][col]))
        stop, input = subtract_one(input)
        if stop:
            break
        output = move_one_layer_down(output)

    while True:
        start_points = left_up_points_negative(len(output) - 1)
        for row in range(2, -1, -1):
            for col in range(2, -1, -1):
                if input[row][col] < 0:
                    output = add_cube_bottom(
                        output,
                        start_of_rows(start_points[row][col]))
        stop, input = add_one(input)
        if stop:
            break

    print(to_txt(output))


if __name__ == '__main__':
    main([[3, 3, 2], [1, 1, 1], [3, 1, 2]])
    main([[1, 1, 1], [1, -1, -3], [-2, 0, 0]])
