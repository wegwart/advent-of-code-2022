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
    
def get_shared_item(a, b, c):
    shared = list(set(a).intersection(b).intersection(c))
    return shared[0]
    
def test_get_shared_item():
    assert(get_shared_item('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFM...ZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg') == 'r')
     
def get_shared_items(file_name):
    with open(file_name) as f:
        shared_items = []
        group_items = []
        for index, line in enumerate(f):
            items = line.strip()
            group_items.append(items)
            if len(group_items) == 3:
                shared_item = get_shared_item(group_items[0], group_items[1], group_items[2])
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

__location__ = pathlib.Path(__file__).parent

def test_puzzle():
    assert(puzzle(__location__ / 'day3_test_part2.txt', verbose=True) ==  70)
    
def print_puzzle():
    print(puzzle(__location__ / 'day3_puzzle_part2.txt'))
    
if __name__ == '__main__':
    test_get_priority()
    test_get_shared_item()
    test_puzzle()
    print_puzzle()