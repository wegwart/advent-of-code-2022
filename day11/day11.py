import pathlib
    
def get_inspected_items(file_name, iterations, is_part2):
    with open(file_name) as f:
        notes = []
        while True:
            n0 = int(f.readline().strip().replace('Monkey', '').replace(':', ''))
            n1 = list(map(int, f.readline().strip().replace('Starting items:','').split(',')))
            n2, n3 = f.readline().strip().split(' ')[4:]
            n4 = int(f.readline().strip().split(' ')[3])
            n5 = int(f.readline().strip().split(' ')[5])
            n6 = int(f.readline().strip().split(' ')[5])
            notes.append((n0, n1, n2, n3, n4, n5, n6))
            if len(f.readline()) < 1:
                break   
    
    if is_part2:        
        # calculate common multiples
        mod = 1
        for note in notes:
            test = note[4]        
            mod *= test
        
    items = [[] for _ in range(len(notes))]
    count_inspecting_items = [0] * len(notes)
    for iteration in range(iterations):
        for note in notes:
            monkey = note[0]
            starting_items = note[1]
            operator = note[2]
            operand = note[3]
            test = note[4]
            if_true = note[5]
            if_false = note[6]
            results = []
            if iteration == 0:
                starting_items += items[monkey]
                items[monkey].clear()        
            else:
                starting_items.clear()
                starting_items += items[monkey]
                items[monkey].clear()                        
            for starting_item in starting_items:
                count_inspecting_items[monkey] += 1
                worry_level = starting_item
                if operand == 'old':
                    operand_value = worry_level
                else:
                    operand_value = int(operand)
                if operator == '+':
                    worry_level += operand_value
                elif operator == '*':
                    worry_level *= operand_value
                if is_part2:
                    worry_level %= mod
                else:
                    worry_level = int(worry_level / 3)
                if  worry_level % test == 0:
                    throw_to = if_true
                else:
                    throw_to = if_false
                results.append((worry_level, throw_to))
                items[throw_to].append(worry_level)
            #print('{} --> {}'.format(note, results))
        #print('{} --> {}'.format(iteration, items))
        if (iteration+1) % 1000 == 0:
            print('{} --> {}'.format(iteration+1, count_inspecting_items)) 
    return count_inspecting_items

def puzzle(file_name, iterations, is_part2, verbose = False):
    inspected_items = get_inspected_items(file_name, iterations, is_part2)
    inspected_items.sort()
    result = inspected_items[-1] * inspected_items[-2]
    if verbose:
        print('{} --> {} --> {}'.format(file_name, inspected_items, result))
    return result

__location__ = pathlib.Path(__file__).parent
   
def test_puzzle():
    assert(puzzle(__location__ / 'day11_test.txt', iterations=20, is_part2=False, verbose=False) == 10605) 

def test_puzzle_part2():
    assert(puzzle(__location__ / 'day11_test.txt', iterations=10000, is_part2=True, verbose=True) == 2713310158) 
          
def print_puzzle():
    print(puzzle(__location__ / 'day11_puzzle.txt', iterations=20, is_part2=False))
              
def print_puzzle_part2():
    print(puzzle(__location__ / 'day11_puzzle.txt', iterations=10000, is_part2=True))
                  
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()
    test_puzzle_part2()
    print_puzzle_part2()    
