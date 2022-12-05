import pathlib
          
def get_intermediate_results(file_name, N):
    with open(file_name) as f:
        crates_list = [[] for i in range(N)]
        init = True
        for index, line in enumerate(f):
            if init:
                if len(line.strip()) == 0:
                    init = False                
                for i in range(N):                
                    try:
                        if line[i*4] == '[':
                            crate = line[i*4+1]
                            crates_list[i].insert(0, crate)
                    except:
                        continue
            else:
                splitted_line = line.split(' ')
                move_count = int(splitted_line[1])
                move_from = int(splitted_line[3])
                move_to = int(splitted_line[5]) 
                move_crates = []
                for i in range(move_count):               
                    crate = crates_list[move_from-1].pop()
                #    move_crates.append(crate)
                #for i in range(move_count):    
                #    crate = move_crates[i]           
                    crates_list[move_to-1].append(crate)
        return crates_list
       
def puzzle(file_name, N, verbose = False):
    intermediate_results = get_intermediate_results(file_name, N)
    result = ''
    for intermediate_result in intermediate_results:
        peek_crate = intermediate_result[-1]
        result += peek_crate
    if verbose:
        print('{} --> {} --> {}'.format(file_name, intermediate_results, result))
    return result

__location__ = pathlib.Path(__file__).parent

def test_puzzle():
    assert(puzzle(__location__ / 'day5_test.txt', 3, verbose=True) ==  'CMZ')
        
def print_puzzle():
    print(puzzle(__location__ / 'day5_puzzle.txt', 9))
       
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()

