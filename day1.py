def get_subtotals(file_name):
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
        return subtotals
    
def puzzle(file_name, verbose = False):
    subtotals = get_subtotals(file_name)
    result = max(subtotals)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, subtotals, result))
    return result

def puzzle_part2(file_name, verbose = False):
    subtotals = get_subtotals(file_name)
    subtotals.sort(reverse=True)
    result = sum(subtotals[0:3])
    if verbose:
        print('{} --> {} --> {}'.format(file_name, subtotals, result))
    return result

if __name__ == '__main__':
    verbose = True
    puzzle('day1_test.txt', verbose)
    puzzle_part2('day1_test.txt', verbose)