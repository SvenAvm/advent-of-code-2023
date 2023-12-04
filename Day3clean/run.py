import utils

input_path = "tests/input.txt"
test1_path = "tests/test1.txt"
test2_path = "tests/test2.txt"

input_grid = utils.parse_file(input_path)
test1_grid = utils.parse_file(test1_path)
test2_grid = utils.parse_file(test2_path)

symbol_locations = utils.find_all_symbol_starting_point_locations(test1_grid, utils.symbol_regex)
asterix_locations = utils.find_all_symbol_starting_point_locations(test1_grid, utils.asterix_regex)
number_starting_locations = utils.find_all_symbol_starting_point_locations(test1_grid, utils.numbers_regex)


print(f" Symbol locations: {symbol_locations}")
print(f" Asterix locations: {asterix_locations}")
print(f" Number locations: {number_starting_locations}")

print(utils.check_if_number_left(test1_grid, (0, 1)))

