import pathlib
       
def get_priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
    
def test_get_priority():
    assert(get_priority('a') == 1)
    assert(get_priority('z') == 26)
    assert(get_priority('A') == 27)
    assert(get_priority('Z') == 52)
    
def get_shared_item(a, b):
    shared = list(set(a).intersection(b))
    return shared[0]

def get_shared_item_part2(a, b, c):
    shared = list(set(a).intersection(b).intersection(c))
    return shared[0]
    
def test_get_shared_item():
    assert(get_shared_item('vJrwpWtwJgWr', 'hcsFMMfFFhFp') == 'p')
    
def test_get_shared_item_part2():
    assert(get_shared_item_part2('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg') == 'r')
   
def get_shared_items(file_name):
    with open(file_name) as f:
        shared_items = []
        for index, line in enumerate(f):
            items = line.strip()
            n = int(len(items)/2)
            first_items = items[:n]
            second_items = items[n:]
            c = sorted(first_items, key=lambda c: get_priority(c))
            d = sorted(second_items, key=lambda c: get_priority(c))
            shared_item = get_shared_item(first_items, second_items)
            shared_items.append(shared_item) 
        return shared_items
    
def get_shared_items_part2(file_name):
    with open(file_name) as f:
        shared_items = []
        group_items = []
        for index, line in enumerate(f):
            items = line.strip()
            group_items.append(items)
            if len(group_items) == 3:
                shared_item = get_shared_item_part2(group_items[0], group_items[1], group_items[2])
                shared_items.append(shared_item)
                group_items.clear()
        return shared_items
    
def puzzle(file_name, verbose = False):
    shared_items = get_shared_items(file_name)
    get_priorities = map(get_priority, shared_items)
    result = sum(get_priorities)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, shared_items, result))
    return result

def puzzle_part2(file_name, verbose = False):
    shared_items = get_shared_items_part2(file_name)
    get_priorities = map(get_priority, shared_items)
    result = sum(get_priorities)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, shared_items, result))
    return result

__location__ = pathlib.Path(__file__).parent

def test_puzzle():
    assert(puzzle(__location__ / 'day3_test.txt', verbose=True) ==  157)
    
def print_puzzle():
    print(puzzle(__location__ / 'day3_puzzle.txt'))
    
def test_puzzle_part2():
    assert(puzzle_part2(__location__ / 'day3_test.txt', verbose=True) ==  70)
    
def print_puzzle_part2():
    print(puzzle_part2(__location__ / 'day3_puzzle.txt'))
    
if __name__ == '__main__':
    test_get_priority()
    test_get_shared_item()
    test_puzzle()
    print_puzzle()
    test_get_shared_item_part2()    
    test_puzzle_part2()
    print_puzzle_part2()