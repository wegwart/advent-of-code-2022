import pathlib
          
def get_item_results(file_name):
    with open(file_name) as f:
        item_results = []
        for index, line in enumerate(f):
            pairs = line.strip().split(',')
            left = list(map(int, pairs[0].split('-')))
            right = list(map(int, pairs[1].split('-')))
            a = list(range(left[0], left[1]+1))
            b = list(range(right[0], right[1]+1))
            c = list(set(a).intersection(b))
            if set(a).issubset(c) or set(b).issubset(c):
                item_results.append(1)
            else:
                item_results.append(0)            
        return item_results
       
def puzzle(file_name, verbose = False):
    item_results = get_item_results(file_name)
    result = sum(item_results)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, item_results, result))
    return result

__location__ = pathlib.Path(__file__).parent

def test_puzzle():
    assert(puzzle(__location__ / 'day4_test.txt', verbose=True) ==  2)
    
def print_puzzle():
    print(puzzle(__location__ / 'day4_puzzle.txt'))
    
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()
