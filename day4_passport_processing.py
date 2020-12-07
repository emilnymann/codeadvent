import re
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

# PART TWO
print('-------------------------\nPART TWO\n-------------------------')

valid_count = 0
passports = []

# parse input into array with seperated key/value pairs
for passport in input:
    passport = passport.replace('\n', ' ')
    passport = passport.split(' ')
    properties = []
    for prop in passport:
        prop = prop.split(':')
        properties.append(prop)
    passports.append(properties)

for passport in passports:
    property_count = 0
    valid = True
    for prop in passport:
        if prop[0] == 'byr':
            property_count += 1
            if not int(prop[1]) >= 1920 or not int(prop[1]) <= 2002:
                valid = False
                break
        elif prop[0] == 'iyr':
            property_count += 1
            if not int(prop[1]) >= 2010 or not int(prop[1]) <= 2020:
                valid = False
                break
        elif prop[0] == 'eyr':
            property_count += 1
            if not int(prop[1]) >= 2020 or not int(prop[1]) <= 2030:
                valid = False
                break
        elif prop[0] == 'hgt':
            property_count += 1
            regex = re.compile('((1[5-8][0-9]|19[0-7])(cm))|((59|6[0-9]|7[0-6])(in))', re.I)
            if not regex.match(prop[1]):
                valid = False
                break
        elif prop[0] == 'hcl':
            property_count += 1
            regex = re.compile('#([0-9]|[a-f]){6}', re.I)
            if not regex.match(prop[1]):
                valid = False
                break
        elif prop[0] == 'ecl':
            property_count += 1
            regex = re.compile('(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)', re.I)
            if not regex.match(prop[1]):
                valid = False
                break
        elif prop[0] == 'pid':
            property_count += 1
            regex = re.compile('[0-9]{9}', re.I)
            if not regex.match(prop[1]) or not len(prop[1]) == 9:
                valid = False
                break
            else:
                print('+VALID PROP (' + prop[0] + '): ' + str(prop[1]))

    if valid == True and property_count == len(match_fields):
        valid_count += 1

print(valid_count)