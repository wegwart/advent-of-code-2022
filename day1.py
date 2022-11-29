def puzzle(file_name):
    with open(file_name) as f:
        lines = 0
        for index, line in enumerate(f):
            lines += 1
        print('{} --> {}'.format(file_name, lines))
        return lines

if __name__ == '__main__':
    assert(puzzle('day1_test.txt') == 2)