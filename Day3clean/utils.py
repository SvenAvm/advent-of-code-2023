import re

symbol_regex = r"[\*\#\+\$\/\&\%\-\@\=]"
numbers_regex = r"\d+"
asterix_regex = r"\*"


# Parse the file into a list of lists to be used by other functions
def parse_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


# Find all desired symbols, use regex to target specific symbol/s
def find_all_symbol_starting_point_locations(grid, symbol_regex):
    results = []
    pattern = re.compile(symbol_regex)
    for row_number, line in enumerate(grid):
        line_str = ''.join(line)  # Convert list of characters to string
        for match in pattern.finditer(line_str):
            results.append((row_number, match.start()))  # Zero-indexed position
    return results


# Search around the target location in all 8 directions and return all matches
def search_around_target_location(grid, target_location, target_regex):
    pass


# Check left and riht for continious digits of a whole number
def check_for_continuous_digits(grid, position):
    pass


# take 2 numbers as input and return their power
def calculate_gear_ratio(whole_number_1, whole_number_2):
    gear_ratio = whole_number_1 * whole_number_2
    return gear_ratio


# Returns True if the given location is a number.
def check_if_number_left(grid, position):
    row, col = position
    # Adjust for 0-indexing
    row -= 1
    col -= 1

    # Check if the column is not the first one and the left cell contains a number
    if col > 0 and grid[row][col - 1].isdigit():
        return True
    else:
        return False


# Returns True if the given location is a number.
def check_if_number_right(grid, position):
    pass


# Returns True if the given location is a number.
def check_if_number_top(grid, position):
    pass


# Returns True if the given location is a number.
def check_if_number_bottom(grid, position):
    pass


# Returns True if the given location is a number.
def check_if_number_top_left(grid, position):
    pass


# Returns True if the given location is a number.
def check_if_number_top_right(grid, position):
    pass


# Returns True if the given location is a number.
def check_if_number_bottom_left(grid, position):
    pass


# Returns True if the given location is a number.
def check_if_number_bottom_right(grid, position):
    pass


# Returns the whole number from a starting position of a single digit.
# It checks left and right, adds all the positions where it finds a number to a list, and then returns the whole number
# Should be used if one of the check_if_number functions returns a position
def return_whole_number(grid, position):
    pass


