import re


def get_calibration_value(line):
    # Find all sequences of digits in the line
    digits = re.findall(r'\d', line)
    if digits:
        # Combine the first and last digit to form a two-digit number
        return int(digits[0] + digits[-1])
    return 0


def sum_calibration_values(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += get_calibration_value(line.strip())
    return total


# Usage
result = sum_calibration_values('puzzle-input.txt')
print(result)
