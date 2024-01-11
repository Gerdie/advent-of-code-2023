race_times = []
race_distances = []
with open('input.txt') as input_file:
    for line in input_file:
        data = line.strip().split()
        if data[0] == 'Time:':
            race_times = data[1:]
        elif data[0] == 'Distance:':
            race_distances = data[1:]

def will_win(race_time, race_distance, hold_time):
    speed = hold_time
    return ((race_time - hold_time) * speed) > race_distance

def lowest_hold_time(race_time, race_distance):
    for hold_time in range(race_time):
        if will_win(race_time, race_distance, hold_time):
            return hold_time

def highest_hold_time(race_time, race_distance):
    for hold_time in range(race_time):
        if will_win(race_time, race_distance, race_time - hold_time):
            return race_time - hold_time

victories = 1
for idx, race_time in enumerate(race_times):
    race_time = int(race_time)
    race_distance = int(race_distances[idx])
    low_time = lowest_hold_time(race_time, race_distance)
    high_time = highest_hold_time(race_time, race_distance)
    number_hold_times = high_time - low_time + 1
    victories = victories * number_hold_times

print('Part One: {}'.format(victories))

race_time = int(''.join(race_times))
race_distance = int(''.join(race_distances))
low_time = lowest_hold_time(race_time, race_distance)
high_time = highest_hold_time(race_time, race_distance)
number_hold_times = high_time - low_time + 1

print('Part Two: {}'.format(number_hold_times))
