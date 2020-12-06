input = open('inputs/day3_input.txt').read().split('\n')

# PART ONE
print('-------------------------\nPART ONE\n-------------------------')

position_x = 0
tree_count = 0

for y in input:
    if y[position_x % len(y)] == '#':
        tree_count += 1
    position_x += 3

print(tree_count)

# PART TWO
print('-------------------------\nPART TWO\n-------------------------')

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree_counts = []
result = 1

for s in slopes:
    position_x = 0
    position_y = 0
    tree_count = 0
    while position_y <= len(input) - 1:
        character = input[position_y][position_x % len(input[position_y])]
        if character == '#':
            tree_count += 1
        # print(character + '(Line ' + str(position_y + 1) + ')')
        position_x += s[0]
        position_y += s[1]
    tree_counts.append(tree_count)

for tc in tree_counts:
    result = result * tc
print(tree_counts)
print('Result: ' + str(result))