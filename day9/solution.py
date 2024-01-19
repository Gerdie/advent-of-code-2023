
def expand_line_array(line_array):
    next_line = []
    all_zeroes = True
    last_line = line_array[-1]
    for idx, num in enumerate(last_line):
        if idx + 1 < len(last_line):
            next_val = last_line[idx+1] - num
            next_line.append(next_val)
            if next_val != 0:
                all_zeroes = False
    line_array.append(next_line)
    if all_zeroes:
        return line_array
    return expand_line_array(line_array)

def get_next_prediction(expanded_line):
    num_lines = len(expanded_line)
    last = 0
    for line_idx in range(num_lines):
        line = expanded_line[num_lines - line_idx - 1]
        last += line[-1]
    return last

def get_prev_prediction(expanded_line):
    num_lines = len(expanded_line)
    last = 0
    for line_idx in range(num_lines):
        line = expanded_line[num_lines - line_idx - 1]
        last = line[0] - last
    return last

with open('input.txt') as input_file:
    next_predicted_sum = 0
    prev_predicted_sum = 0
    for line in input_file:
        line = list(map(int, line.strip().split()))
        expanded = expand_line_array([line])
        next_prediction = get_next_prediction(expanded)
        next_predicted_sum += next_prediction
        prev_prediction = get_prev_prediction(expanded)
        prev_predicted_sum += prev_prediction

    print('Part One: {}'.format(next_predicted_sum))
    print('Part Two: {}'.format(prev_predicted_sum))
