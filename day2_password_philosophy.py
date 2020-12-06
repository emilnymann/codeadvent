input = open('inputs/day2_input.txt', 'r').read().split('\n')

item_array = []
for i in input:
    item = i.split(': ')
    password = item[1]
    protocol = item[0].split(' ')
    match_letter = protocol[1]
    min_max = protocol[0].split('-')
    min = int(min_max[0])
    max = int(min_max[1])
    item_dict = dict(min = min, max = max, match = match_letter, password = password)
    item_array.append(item_dict)

# PART ONE
print('--------------------------\nPART ONE\n--------------------------')

valid_count = 0

for i in item_array:
    match_count = i['password'].count(i['match'])
    if match_count >= i['min'] and match_count <= i['max']:
        valid_count += 1

print('Result: ' + str(valid_count))

# PART TWO
print('--------------------------\nPART TWO\n--------------------------')

valid_count = 0

for i in item_array:
    match_count = 0
    if i['password'][i['min'] - 1] == i['match']:
        match_count += 1
    if i['password'][i['max'] - 1] == i['match']:
        match_count += 1
    if match_count == 1:
        valid_count += 1

print('Result: ' + str(valid_count))