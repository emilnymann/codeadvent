# PART ONE

input_file = open('inputs/day_report_repair.txt', 'r')
input_data = input_file.read().split('\n')
input_data = [int(x) for x in input_data]
input_data.sort()

target = 2020

for p in input_data:
    for p2 in input_data:
        if p != p2:
            if p + p2 == target:
                print("Solution found. " + str(p) + " * " + str(p2) + " = " + str(p * p2))

# PART TWO

print("--------------------\nPART TWO\n--------------------")
for p in input_data:
    for p2 in input_data:
        for p3 in input_data:
            if p != p2 and p != p3 and p2 != p3:
                if p + p2 + p3 == target:
                    print("Solution found. " + str(p) + " * " + str(p2) + " * " + str(p3) + " = " + str(p * p2 * p3))