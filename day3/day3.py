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
    
def test_get_shared_item():
    assert(get_shared_item('vJrwpWtwJgWr', 'hcsFMMfFFhFp') == 'p')
     
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
    
def puzzle(file_name, verbose = False):
    shared_items = get_shared_items(file_name)
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
    
if __name__ == '__main__':
    test_get_priority()
    test_get_shared_item()
    test_puzzle()
    print_puzzle()