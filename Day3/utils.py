import re

# Regular expression to match specified symbols
symbol_reg = r"[\*\#\+\$\/\&\%\-\@\=]"


def find_symbols(grid, target_regex):
    results = []
    pattern = re.compile(target_regex)
    for row_number, line in enumerate(grid):
        line_str = ''.join(line)  # Convert list of characters to string
        for match in pattern.finditer(line_str):
            results.append((row_number, match.start()))  # Zero-indexed position
    return results


def get_surrounding_numbers(grid, symbol_position):
    def get_full_number_from_position(rows, columns):
        # Start with the number at the current position
        whole_number = grid[rows][columns]
        start_col = columns  # Remember the starting column of the number

        # Check to the left
        i = columns - 1
        while i >= 0 and grid[rows][i].isdigit():
            whole_number = grid[rows][i] + whole_number
            start_col = i  # Update the starting column
            i -= 1

        # Check to the right
        i = columns + 1
        while i < len(grid[rows]) and grid[rows][i].isdigit():
            whole_number += grid[rows][i]
            i += 1

        return whole_number, (rows, start_col)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    row, col = symbol_position[0], symbol_position[1]
    found_numbers = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col].isdigit():
            full_number, number_position = get_full_number_from_position(new_row, new_col)
            found_numbers.append((full_number, number_position))

    return found_numbers
