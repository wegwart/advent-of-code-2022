import pathlib
          
def is_marker(synch):
    duplicates = list(filter(lambda x: synch.count(x) >= 2, synch))
    return len(duplicates) == 0   
    
def get_intermediate_results(file_name, is_part2):
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
            if is_part2:
                if len(synch) > 14:
                    synch = synch[1:]
                if len(synch) == 14:
                    if is_marker(synch):
                        result.append(len(buffer))
                        buffer = ''
                        synch = ''                    
            else:
                if len(synch) > 4:
                    synch = synch[1:]
                if len(synch) == 4:
                    if is_marker(synch):
                        result.append(len(buffer))
                        buffer = ''
                        synch = ''                    
    return result

def puzzle(file_name, is_part2, verbose = False):
    intermediate_results = get_intermediate_results(file_name, is_part2)
    result = intermediate_results[0]
    if verbose:
        print('{} --> {} --> {}'.format(file_name, intermediate_results, result))
    return result

__location__ = pathlib.Path(__file__).parent

def test_puzzle():
    assert(puzzle(__location__ / 'day6_test.txt', False, verbose=True) == 7)
        
def test_puzzle_part2():
    assert(puzzle(__location__ / 'day6_test.txt', True, verbose=True) == 19)
            
def print_puzzle():
    print(puzzle(__location__ / 'day6_puzzle.txt', False))
          
def print_puzzle_part2():
    print(puzzle(__location__ / 'day6_puzzle.txt', True))
              
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()
    test_puzzle_part2()
    print_puzzle_part2()
