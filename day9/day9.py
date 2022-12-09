import pathlib
import matplotlib.pyplot as plt
  
def get_intermediate_results(file_name, knots, verbose):
    with open(file_name) as f:
        motions = []
        for index, line in enumerate(f):
            motion = line.strip().split(' ')
            motions.append(motion)
    K = knots
    x, y = [0] * K, [0] * K
    tail_positions = []
    for motion in motions:        
        direction = motion[0]
        steps = int(motion[1])
        if verbose:
            print('\n{} {} '.format(direction, steps), end='')
        for step in range(steps):
            for k in range(K):        
                if k == 0:
                    if direction == 'R':
                        x[k] += 1  
                    elif direction == 'L':
                        x[k] -= 1
                    elif direction == 'U':
                        y[k] += 1                
                    elif direction == 'D':
                        y[k] -= 1  
                    if verbose:
                        print('\n{}={},{} '.format('H', x[k], y[k]), end='')
                    continue
                dx = x[k-1] - x[k] 
                dy = y[k-1] - y[k]
                if abs(dx) == 2 and abs(dy) == 0:
                    x[k] += int(dx/2)
                elif abs(dx) == 0 and abs(dy) == 2:
                    y[k] += int(dy/2)
                elif abs(dx) == 2 and abs(dy) == 2:
                    x[k] += int(dx/2)
                    y[k] += int(dy/2)                    
                elif abs(dx) == 2 and abs(dy) == 1:
                    x[k] += int(dx/2)
                    y[k] += dy
                elif abs(dx) == 1 and abs(dy) == 2:
                    x[k] += dx
                    y[k] += int(dy/2)
                if verbose:                        
                    print('{}={},{} '.format(k, x[k], y[k]), end='')                                        
                if k == K-1:
                    tail_positions.append((x[k],y[k]))
    return tail_positions

def puzzle(file_name, knots, verbose = False, plot = False):
    tail_positions = get_intermediate_results(file_name, knots, verbose)
    unique_tail_positions = dict()
    for tail_position in tail_positions:
        unique_tail_positions[tail_position] = unique_tail_positions.get(tail_position, 0) + 1
    result = len(unique_tail_positions)
    if plot:
        transpose_unique_tail_positions = list(zip(*unique_tail_positions.keys()))
        x = transpose_unique_tail_positions[0]
        y = transpose_unique_tail_positions[1]
        fig, ax = plt.subplots()   
        ax.plot(x, y, 'ro')
        plt.grid()
        plt.show(block=True)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, unique_tail_positions, result))
    return result

__location__ = pathlib.Path(__file__).parent
   
def test_puzzle():
    assert(puzzle(__location__ / 'day9_test.txt', 2, verbose=False) == 13) 

def test_puzzle_part2():
    assert(puzzle(__location__ / 'day9_test.txt', 10, verbose=False) == 1)
    assert(puzzle(__location__ / 'day9_test_part2.txt', 10, verbose=False) == 36)
            
def print_puzzle():
    print(puzzle(__location__ / 'day9_puzzle.txt', 2))
          
def print_puzzle_part2():
    print(puzzle(__location__ / 'day9_puzzle.txt', 10))
              
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()
    test_puzzle_part2()
    print_puzzle_part2()
    