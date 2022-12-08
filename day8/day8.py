import pathlib
          
def is_visible(heights, selected_idx):
    result_before = True
    result_after = True
    selected_height = heights[selected_idx]
    for index, height in enumerate(heights):        
        if index != selected_idx:
            if height >= selected_height:
                if index < selected_idx:
                    result_before = False
                else:
                    result_after = False                
    return result_before or result_after
   
def get_score(heights, selected_idx):
    heights_right = heights[selected_idx+1:]
    heights_left = list(reversed(heights[:selected_idx]))
    selected_height = heights[selected_idx]
    score_right = 0
    for height in heights_right:
        score_right += 1
        if height >= selected_height:
            break            
    score_left = 0
    for height in heights_left:
        score_left += 1
        if height >= selected_height:
            break            
    return score_right * score_left
   
def get_results_map(file_name, is_part2):
    with open(file_name) as f:
        heights_map = []
        for index, line in enumerate(f):
            heights_row = list(map(int, list(line.strip())))
            heights_map.append(heights_row)
    rows = len(heights_map)
    cols = len(heights_map[0])
    heights_map_transposed = list(zip(*heights_map))
    results_map = []
    for row in range(rows):
        results = []
        for col in range(cols):
            heights_row = heights_map[row]
            heights_col = heights_map_transposed[col]
            if is_part2:
                score_left_right = get_score(heights_row, col)
                score_up_down = get_score(heights_col, row)
                results.append(score_left_right * score_up_down)
            else:
                is_visible_from_left_or_right = is_visible(heights_row, col)
                is_visible_from_top_or_down = is_visible(heights_col, row)
                results.append(int(is_visible_from_left_or_right or is_visible_from_top_or_down))
        results_map.append(results)
    return results_map

def puzzle(file_name, is_part2, verbose = False):
    results_map = get_results_map(file_name, is_part2)
    result = 0
    for results in results_map:
        if is_part2:
            if max(results) > result:
                result = max(results)
        else:
            result += sum(results)
    if verbose:
        print('{} --> {} --> {}'.format(file_name, results_map, result))
    return result

__location__ = pathlib.Path(__file__).parent
   
def test_puzzle():
    assert(puzzle(__location__ / 'day8_test.txt', False, verbose=True) == 21)
   
def test_get_score():
    # middle 5 in the second row
    assert(get_score([2, 5, 5, 1, 2], 2) == 2)
    assert(get_score([3, 5, 3, 5, 3], 1) == 2) 
    # tree of height 5 in the middle of the fourth row
    assert(get_score([3, 3, 5, 4, 9], 2) == 4)
    assert(get_score([3, 5, 3, 5, 3], 3) == 2) 
            
def test_puzzle_part2():
    assert(puzzle(__location__ / 'day8_test.txt', True, verbose=True) == 8)
            
def print_puzzle():
    print(puzzle(__location__ / 'day8_puzzle.txt', False))
          
def print_puzzle_part2():
    print(puzzle(__location__ / 'day8_puzzle.txt', True))
              
if __name__ == '__main__':
    test_puzzle()
    print_puzzle()
    test_get_score()
    test_puzzle_part2()
    print_puzzle_part2()
    