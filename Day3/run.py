import utils

file_path_test = 'test.txt'
file_path_test2 = 'test2.txt'
file_path_task = 'input.txt'


# Function to process a file and calculate the sum of unique numbers around symbols
def process_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    symbol_positions = utils.find_symbols(grid, utils.symbol_reg)
    all_found_numbers_with_position = set()

    for symbol_position in symbol_positions:
        surrounding_numbers = utils.get_surrounding_numbers(grid, symbol_position)
        for number, pos in surrounding_numbers:
            all_found_numbers_with_position.add((number, pos))  # Add both number and position

    # Calculate the sum considering unique number-position pairs
    sum_of_numbers = sum(int(number) for number, pos in all_found_numbers_with_position)
    return sum_of_numbers


# Processing the files and calculating the sums
sum_test = process_file(file_path_test)
sum_test2 = process_file(file_path_test2)
sum_task = process_file(file_path_task)

print("Sum for test.txt:", sum_test)
print("Sum for test2.txt:", sum_test2)
print("Sum for input.txt:", sum_task)

asterix_surrounded = utils.find_asterisks_surrounded_by_numbers()