import re
import utils


pattern = '|'.join([f'({word})' for word in utils.number_words.keys()]) + r'|\d'
reversed_pattern = '|'.join([f'({word})' for word in utils.reversed_number_words.keys()]) + r'|\d'


def find_first_number(input_string):
    # mapping of number words to their numeric values

    # loop through the string to find the first match
    for match in re.finditer(pattern, input_string):
        num = match.group()
        if num.isdigit():
            return int(num)
        elif num in utils.number_words:
            return int(utils.number_words[num])


def find_second_number(input_string):
    # mapping of number words to their numeric values

    # loop through the string to find the first match
    for match in re.finditer(reversed_pattern, input_string):
        num = match.group()
        if num.isdigit():
            return int(num)
        elif num in utils.reversed_number_words:
            return int(utils.reversed_number_words[num])


def sum_calibration_values(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            first_number = find_first_number(line)
            second_number = find_second_number(line[::-1])

            # check if both numbers are not None
            if first_number is not None and second_number is not None:
                total += int(f"{first_number}{second_number}")
            else:
                total += 0

    return total


print(sum_calibration_values("../puzzle-input.txt"))



