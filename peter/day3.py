import collections


lines = open("inputs/day3.txt").read().strip().split("\n")

ints = [[int(c) for c in line] for line in lines]
columns = list(zip(*ints))
column_counts = [collections.Counter(column) for column in columns]


def most_common(counter):
    return 1 if counter[1] >= counter[0] else 0


def least_common(counter):
    return 0 if counter[0] <= counter[1] else 1


gamma = [most_common(counter) for counter in column_counts]
epsilon = [least_common(counter) for counter in column_counts]


def to_decimal(binary):
    n = 0
    for i, b in enumerate(reversed(binary)):
        n += (2 ** i) * b
    return n


print("Part 1:", to_decimal(gamma) * to_decimal(epsilon))


def find_oxygen_number(all_numbers, column_counts):
    filtered_numbers = all_numbers
    position = 0
    while len(filtered_numbers) > 1:
        columns = list(zip(*filtered_numbers))
        counter = collections.Counter(columns[position])
        filtered_numbers = [f for f in filtered_numbers if int(f[position]) == most_common(counter)]
        position += 1
    return filtered_numbers[0]


def find_co2_number(all_numbers, column_counts):
    filtered_numbers = all_numbers
    position = 0
    while len(filtered_numbers) > 1:
        columns = list(zip(*filtered_numbers))
        counter = collections.Counter(columns[position])
        filtered_numbers = [f for f in filtered_numbers if int(f[position]) == least_common(counter)]
        position += 1
    return filtered_numbers[0]


o2 = find_oxygen_number(ints, column_counts)
co2 = find_co2_number(ints, column_counts)
print("Part 2:", to_decimal(o2) * to_decimal(co2))
