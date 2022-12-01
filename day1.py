def puzzle(file_name):
    with open(file_name) as f:  
        subtotal = 0
        subtotals = []    
        for index, line in enumerate(f):
            if line == '\n':
                subtotals.append(subtotal)
                subtotal = 0
                continue
            value = int(line)
            subtotal += value
        subtotals.append(subtotal)
        print('{} --> {} --> {}'.format(file_name, subtotals, max(subtotals)))
        return max(subtotals)

if __name__ == '__main__':
    assert(puzzle('day1_test.txt') == 24000)