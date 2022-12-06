import pathlib
          
def is_marker(synch):
    duplicates = list(filter(lambda x: synch.count(x) >= 2, synch))
    return len(duplicates) == 0   
    
def get_intermediate_results(file_name):
    with open(file_name) as f:
        result = []
        buffer = ''
        synch = ''        
        while True:
            c = f.read(1)
            if not c:
                break
            synch += c
            buffer += c
            if len(synch) > 4:
                synch = synch[1:]
                if is_marker(synch):
                    result.append(len(buffer))
                    buffer = ''
                    synch = ''                    
    return result

def puzzle(file_name, verbose = False):
    intermediate_results = get_intermediate_results(file_name)
    result = intermediate_results[0]
    if verbose:
        print('{} --> {} --> {}'.format(file_name, intermediate_results, result))
    return result

__location__ = pathlib.Path(__file__).parent

def test_puzzle():
    assert(puzzle(__location__ / 'day6_test.txt', verbose=True) == 5)
        
def print_puzzle():
    print(puzzle(__location__ / 'day6_puzzle.txt'))
          
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()

