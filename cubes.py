cube = [
    list('x + + + x'),
    list('/       /+'),
    list('/       / +'),
    list('x + + + x  +'),
    list('+       +  x'),
    list('+       + /'),
    list('+       +/'),
    list('x + + + x'),
]

left_up_points = [
    [(0, 9), (0, 17), (0, 25)],
    [(3, 6), (3, 14), (3, 22)],
    [(6, 3), (6, 11), (6, 19)],
]

#     [(3, 6), (3, 14), (3, 22)],
#     [(6, 3), (6, 11), (6, 19)],
#     [(9, 0), (9, 8), (9, 16)],


def start_of_rows(left_up_point):
    shifts = (0, 1, 2, 3, 3, 3, 3, 3)
    row, col = left_up_point
    result = []
    for ind, shift in enumerate(shifts):
        result.append((row + ind, col - shift))
    return result


def add_cube(output, start_of_rows):
    for ind, (row, col) in enumerate(start_of_rows):
        output[row][col:col + len(cube[ind])] = cube[ind]
    return output


def to_txt(output):
    return '\n'.join(''.join(row) for row in output)


def move_1_layer_down(output):
    return [[' '] * 34 for _ in range(4)] + output


def substract_1(input):
    for row in range(3):
        for col in range(3):
            if input[row][col] > 0:
                input[row][col] -= 1
    stop = all(all(each <= 0 for each in row) for row in input)
    return stop, input


def main(input):
    output = [
        [' '] * 34 for _ in range(14)
    ]

    while True:
        for row in range(3):
            for col in range(3):
                if input[row][col] >= 1:
                    output = add_cube(
                        output,
                        start_of_rows(left_up_points[row][col]))
        stop, input = substract_1(input)
        if stop:
            break
        output = move_1_layer_down(output)

    print(to_txt(output))


if __name__ == '__main__':
    main([[3, 3, 2], [1, 1, 1], [3, 1, 2]])
    main([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
