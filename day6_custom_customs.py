input = open('inputs/day6_input.txt', 'r').read().split('\n\n')
groups = []
for i in input:
    group = i.split('\n')
    groups.append(group)

# PART ONE
print('-------------------------\nPART ONE\n-------------------------')

count = 0
for group in groups:
    letters = ''
    for form in group:
        for letter in form:
            if not letter in letters:
                count += 1
                letters += letter

print(count)

# PART TWO
print('-------------------------\nPART TWO\n-------------------------')

count = 0
for group in groups:
    combined_answers = ''
    for form in group[1:]:
        combined_answers += form
    for answer in group[0]:
        if combined_answers.count(answer) == len(group) - 1:
            count += 1

print(count)
