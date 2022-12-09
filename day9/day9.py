import pathlib
import matplotlib.pyplot as plt
  
def get_intermediate_results(file_name, knots):
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
        for step in range(steps):
            for k in range(K-1):        
                if k == 0:
                    match direction:
                        case 'R':
                            x[k] += 1  
                        case 'L':
                            x[k] -= 1
                        case 'U':
                            y[k] += 1                
                        case 'D':
                            y[k] -= 1                    
                move_diagonally = x[k] != x[k+1] and y[k] != y[k+1]
                if x[k] == x[k+1] + 2:
                    x[k+1] += 1
                    if move_diagonally:
                        y[k+1] = y[k]
                elif x[k] == x[k+1] - 2:
                    x[k+1] -= 1
                    if move_diagonally:
                        y[k+1] = y[k]
                if y[k] == y[k+1] + 2:
                    y[k+1] += 1
                    if move_diagonally:
                        x[k+1] = x[k]
                elif y[k] == y[k+1] - 2:
                    y[k+1] -= 1
                    if move_diagonally:
                        x[k+1] = x[k]
                if k == K-2:
                    position = (x[k+1],y[k+1])
                    tail_positions.append(position)
    return tail_positions

def puzzle(file_name, knots, verbose = False, plot = False):
    tail_positions = get_intermediate_results(file_name, knots)
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
        plt.show(block=False)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, unique_tail_positions, result))
    return result

__location__ = pathlib.Path(__file__).parent
   
def test_puzzle():
    assert(puzzle(__location__ / 'day9_test.txt', 2, verbose=True) == 13) 

def test_puzzle_part2():
    assert(puzzle(__location__ / 'day9_test.txt', 10, verbose=True) == 1)
    assert(puzzle(__location__ / 'day9_test_part2.txt', 10, verbose=True) == 36)
            
def print_puzzle():
    print(puzzle(__location__ / 'day9_puzzle.txt', 2))
          
def print_puzzle_part2():
    print(puzzle(__location__ / 'day9_puzzle.txt', 10))
              
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()
    test_puzzle_part2()
    print_puzzle_part2()
    