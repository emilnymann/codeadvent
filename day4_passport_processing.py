input = open('inputs/day4_input.txt', 'r').read().split('\n\n')

# PART ONE
print('-------------------------\nPART ONE\n-------------------------')

match_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_count = 0

for passport in input:
    valid = True
    for match in match_fields:
        if passport.find(match + ':') == -1:
            valid = False
            break
    if valid == True:
        valid_count += 1

print(valid_count)