import pathlib
#import matplotlib.pyplot as plt
  
def get_intermediate_results(file_name, is_part2):
    with open(file_name) as f:
        motions = []
        for index, line in enumerate(f):
            motion = line.strip().split(' ')
            motions.append(motion)
    hx, hy = 0, 0
    tx, ty = 0, 0
    rx, ry = 0, 0
    tails = []
    txs = []
    tys = []
    tails = dict()    
    #fig, ax = plt.subplots()    
    for motion in motions:
        direction = motion[0]
        steps = int(motion[1])
        for step in range(steps):
            hx_old, hy_old = hx, hy
            match direction:
                case 'R':
                    hx += 1              
                case 'L':
                    hx -= 1
                case 'U':
                    hy += 1                
                case 'D':
                    hy -= 1
            move_diagonally = hx != tx and hy != ty                
            if hx == tx + 2:
                tx += 1
                if move_diagonally:
                    ty = hy                
            elif hx == tx - 2:
                tx -= 1
                if move_diagonally:
                    ty = hy                
            if hy == ty + 2:
                ty += 1
                if move_diagonally:
                    tx = hx                    
            elif hy == ty - 2:
                ty -= 1
                if move_diagonally:
                    tx = hx                
            txs.append(tx)
            tys.append(ty) 
            position = (tx, ty)
            tails[position] = 1
    #ax.plot(txs, tys, 'ro')
    #plt.grid()
    #plt.show(block=False)        
    return tails

def puzzle(file_name, is_part2, verbose = False):
    intermediate_results = get_intermediate_results(file_name, is_part2)
    result = len(intermediate_results)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, intermediate_results, result))
    return result

__location__ = pathlib.Path(__file__).parent
   
def test_puzzle():
    assert(puzzle(__location__ / 'day9_test.txt', False, verbose=True) == 13) 

def test_puzzle_part2():
    assert(puzzle(__location__ / 'day9_test.txt', True, verbose=True) == 8)
            
def print_puzzle():
    print(puzzle(__location__ / 'day9_puzzle.txt', False))
          
def print_puzzle_part2():
    print(puzzle(__location__ / 'day9_puzzle.txt', True))
              
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()
    #test_puzzle_part2()
    #print_puzzle_part2()
    