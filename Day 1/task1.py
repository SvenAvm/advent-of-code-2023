import re


def get_calibration_value(line):
    # Find all sequences of numbers in the line
    numbers = re.findall(r'\d', line)
    if numbers:
        # Combine the first and last digit to form a two-digit number
        return int(numbers[0] + numbers[-1])
    return 0


def sum_calibration_values(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += get_calibration_value(line.strip())
    return total


result = sum_calibration_values('input.txt')
print(result)
