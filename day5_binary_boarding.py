import math
input = open('inputs/day5_input.txt', 'r').read().split('\n')

# PART ONE
print('-------------------------\nPART ONE\n-------------------------')

boarding_passes = []
highest_id = 0

for boarding_pass in input:
    row = 0
    column = 0
    row_range = [0, 127]
    column_range = [0, 7]
    for letter in boarding_pass[:-3]:
        if letter == 'F':
            row_range[1] = math.floor((row_range[1] + row_range[0]) / 2)
        elif letter == 'B':
            row_range[0] = math.ceil((row_range[1] + row_range[0]) / 2)
        row = row_range[0]
    for letter in boarding_pass[-3:]:
        if letter == 'L':
            column_range[1] = math.floor((column_range[1] + column_range[0]) / 2)
        elif letter == 'R':
            column_range[0] = math.ceil((column_range[1] + column_range[0]) / 2)
        column = column_range[0]
    seat_id = row * 8 + column
    if seat_id > highest_id:
        highest_id = seat_id
    seat = dict(row = row, col = column, id = seat_id)
    boarding_passes.append(seat)

print('Highest seat ID: ' + str(highest_id))

# PART TWO
print('-------------------------\nPART TWO\n-------------------------')

def sort_by_id(e):
    return e['id']

boarding_passes.sort(reverse=False, key=sort_by_id)

min = boarding_passes[0]['id']
max = boarding_passes[-1]['id']
iteration = 1
result = 0

for bp in boarding_passes:
    if boarding_passes[iteration]['id'] != min + 1:
        result = boarding_passes[iteration]['id'] - 1
        print(str(boarding_passes[iteration]['id']) + ' does not equal ' + str(min + 1))
        break
    elif boarding_passes[iteration * -1]['id'] != max:
        result = boarding_passes[iteration * -1]['id'] + 1
        print(str(boarding_passes[iteration * -1]['id']) + ' does not equal ' + str(max))
        break
    
    min += 1
    max -= 1
    iteration += 1

print('Seat ID is ' + str(result))