seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

def add_seed_data(map_to, map_from, parsing_stage):
    parse_to = parsing_stage[0]
    mapping = None
    if parse_to == 'seed':
        mapping = seed_to_soil
    elif parse_to == 'soil':
        mapping = soil_to_fertilizer
    elif parse_to == 'fertilizer':
        mapping = fertilizer_to_water
    elif parse_to == 'water':
        mapping = water_to_light
    elif parse_to == 'light':
        mapping = light_to_temperature
    elif parse_to == 'temperature':
        mapping = temperature_to_humidity
    elif parse_to == 'humidity':
        mapping = humidity_to_location
    mapping[map_to] = map_from
    return

def parse_seeds(line):
    line = line.strip('seeds: ')
    seeds = set(map(int, line.split()))
    return seeds

def parse_map(line):
    line = list(map(int, line.split()))
    dest_start, source_start, ranges = line
    return dest_start, source_start, ranges

with open('input.txt') as input_file:
    seeds = None
    parsing_stage = None
    looking_for = set()
    found = set()
    for line in input_file:
        line = line.strip()
        if not line:
            continue
        if not seeds and line.startswith('seeds:'):
            seeds = parse_seeds(line)
            continue
        if line.endswith('map:'):
            print(line)
            for item in looking_for:
                found.add(item)
                add_seed_data(item, item, parsing_stage)
            line = line[:-5]
            parsing_stage = line.split('-to-')
            looking_for = found or seeds
            found = set()
            continue
        if not looking_for:
            continue
        dest_start, source_start, ranges = parse_map(line)
        vals_to_pop = []
        for val in looking_for:
            if val >= source_start and val < source_start + ranges:
                offset = val - source_start
                result = dest_start + offset
                found.add(result)
                vals_to_pop.append(val)
                add_seed_data(val, result, parsing_stage)
        for val in vals_to_pop:
            looking_for.remove(val)
    if found and looking_for:
        for item in looking_for:
            found.add(item)
            add_seed_data(item, item, parsing_stage)

lowest_location = None
for hum in humidity_to_location:
    if lowest_location is None:
        lowest_location = humidity_to_location[hum]
        continue
    if humidity_to_location[hum] < lowest_location:
        lowest_location = humidity_to_location[hum]


print('Lowest location: {}'.format(lowest_location))
