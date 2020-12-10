input = open('inputs/day10_input.txt', 'r').read().split('\n')
adapters = [int(x) for x in input]
adapters.sort()
device = adapters[-1] + 3

# PART ONE
print('-------------------------\nPART ONE\n-------------------------')

differences = []

differences.append(adapters[0])

iteration = 1
for adapter in adapters:
    if not iteration == len(adapters):
        difference = adapters[iteration] - adapter
        differences.append(difference)
        iteration += 1

differences.append(device - adapters[-1])
num_one_jolt = differences.count(1)
num_three_jolt = differences.count(3)
result = num_one_jolt * num_three_jolt
print(result)

# PART TWO
print('-------------------------\nPART TWO\n-------------------------')

result = {0:1}

for adapter in adapters:
    result[adapter] = 0
    if adapter - 1 in result:
        result[adapter] += result[adapter - 1]
    if adapter - 2 in result:
        result[adapter] += result[adapter - 2]
    if adapter - 3 in result:
        result[adapter] += result[adapter - 3]

print(result[max(adapters)])