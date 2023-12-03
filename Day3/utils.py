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
    def get_full_number_from_position(row, col):
        # Start with the number at the current position
        whole_number = grid[row][col]
        start_col = col  # Remember the starting column of the number

        # Check to the left
        i = col - 1
        while i >= 0 and grid[row][i].isdigit():
            whole_number = grid[row][i] + whole_number
            start_col = i  # Update the starting column
            i -= 1

        # Check to the right
        i = col + 1
        while i < len(grid[row]) and grid[row][i].isdigit():
            whole_number += grid[row][i]
            i += 1

        return whole_number, (row, start_col)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    row, col = symbol_position[0], symbol_position[1]
    found_numbers = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col].isdigit():
            full_number, number_position = get_full_number_from_position(new_row, new_col)
            found_numbers.append((full_number, number_position))

    return found_numbers


def find_asterisks_surrounded_by_numbers(grid, found_numbers):
    asterisks_surrounded = []
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '*':
                # Check horizontally, vertically, and diagonally for numbers surrounding the asterisk
                adjacent_numbers = []
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 directions
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col].isdigit():
                        adjacent_numbers.append(grid[new_row][new_col])

                # Check if both adjacent numbers are in found_numbers
                if len(adjacent_numbers) == 2 and all(num in found_numbers for num in adjacent_numbers):
                    asterisks_surrounded.append((row + 1, col + 1))  # Add the position of the asterisk (1-indexed)

    return asterisks_surrounded
