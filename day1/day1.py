import pathlib

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

__location__ = pathlib.Path(__file__).parent

def test_puzzle():
    assert(puzzle(__location__ / 'day1_test.txt', verbose=True) == 24000)
  
def print_puzzle():   
    print(puzzle(__location__ / 'day1_puzzle.txt'))
    
def test_puzzle_part2():
    assert(puzzle_part2(__location__ / 'day1_test.txt', verbose=True) == 45000)
    
def print_puzzle_part2():
    print(puzzle_part2(__location__ / 'day1_puzzle.txt'))
    
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()
    test_puzzle_part2()
    print_puzzle_part2()