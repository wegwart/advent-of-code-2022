def decode(code):
    if code in ['A', 'X']:
        select = 'Rock'
    if code in ['B', 'Y']:
        select = 'Paper'
    if code in ['C', 'Z']:
        select = 'Scissors'
    return select

def decode_end(a):
    if a == 'X':
        end = 'lose'
    if a == 'Y':
        end = 'draw'
    if a == 'Z':
        end = 'win'    
    return end

def get_response(opponent, end):
    if end == 'lose':
        if opponent == 'Rock':
            you = 'Scissors'
        elif opponent == 'Scissors':
            you = 'Paper'
        elif opponent == 'Paper':
            you = 'Rock'
    elif end == 'draw':
        you = opponent
    elif end == 'win':
        if opponent == 'Scissors':
            you = 'Rock'
        elif opponent == 'Paper':
            you = 'Scissors'
        elif opponent == 'Rock':
            you = 'Paper'        
    return you
    
def get_score(a, b):
    if a == 'Rock':
        score = 1
    if a == 'Paper':
        score = 2
    if a == 'Scissors':
        score = 3
    if a == b:
        score += 3 # draw
    elif a == 'Rock' and b == 'Scissors' or a == 'Scissors' and b == 'Paper' or a == 'Paper' and b == 'Rock':
        score += 6 # won
    return score
        
def get_scores(file_name):
    with open(file_name) as f:
        scores = []
        for index, line in enumerate(f):
            selection = line.strip().split(' ')
            opponent = decode(selection[0])
            you = decode(selection[1])
            scores.append(get_score(you, opponent))      
        return scores
    
def get_scores_part2(file_name):
    with open(file_name) as f:
        scores = []
        for index, line in enumerate(f):
            selection = line.strip().split(' ')
            opponent = decode(selection[0])
            end = decode_end(selection[1])
            you = get_response(opponent, end)
            scores.append(get_score(you, opponent))        
        return scores
    
def puzzle(file_name, verbose = False):
    scores = get_scores(file_name)
    result = sum(scores)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, scores, result))
    return result
    
def puzzle_part2(file_name, verbose = False):
    scores = get_scores_part2(file_name)
    result = sum(scores)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, scores, result))
    return result

if __name__ == '__main__':
    verbose = True
    puzzle('day2_test.txt', verbose)
    puzzle_part2('day2_test.txt', verbose)