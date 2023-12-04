word_to_num = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_calibration(line):
    first_val = None
    last_val = None
    for char in line:
        if char.isdigit():
            last_val = char
            if first_val is None:
                first_val = char
    return int(first_val + last_val)

def get_calibration2(line):
    first_val = None
    last_val = None
    for idx, char in enumerate(line):
        if char.isdigit():
            last_val = char
            if first_val is None:
                first_val = char
            continue
        wordnums = word_to_num.keys()
        for wordnum in wordnums:
            if line[:idx + 1].endswith(wordnum):
                num = word_to_num[wordnum]
                last_val = num
                if first_val is None:
                    first_val = num
                continue

    return int(first_val + last_val)


with open('input.txt') as file:
    total = 0
    total2 = 0
    for line in file:
        line = line.strip()
        calibration_value = get_calibration(line)
        total += calibration_value
        calibration_value2 = get_calibration2(line)
        total2 += calibration_value2
    print('Part 1: {}'.format(total))
    print('Part 2: {}'.format(total2))