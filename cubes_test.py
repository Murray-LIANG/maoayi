

empty = [
    '            ',
    '            ',
    '            ',
    '            ',
    '            ',
    '            ',
    '            ',
    '            ',
]

cube = [
    '   + + + + +',
    '  /       /+',
    ' /       / +',
    '+ + + + +  +',
    '+       +  +',
    '+       +  /',
    '+       + / ',
    '+ + + + +   ',
]

all_cubes = [
    '',
    '',
    '',
]




def append_cube(c1, c2):
    if c1 == '':
        return c2
    result = []
    if c2 == '':
        for _, row in enumerate(c1):
            result.append(row + ' ' * 8)
    else:
        shift = [1, 2, 3, 4, 4, 4, 3, 1]
        for index, num in enumerate(shift):
            result.append(''.join(list(c1[index])[:-num]) + c2[index].strip())

    return result

c = append_cube(cube, cube)
print('\n'.join(c))
c = append_cube(c, cube)
print('\n'.join(c))
