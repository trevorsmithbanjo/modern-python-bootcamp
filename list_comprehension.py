numbers = [1, 2, 3, 4, 5, 6]
doubled_numbers = [num * 2 for num in numbers]

print('doubled_numbers')
print(doubled_numbers)

print('multiply numbers in a range by 10')
print([num * 10 for num in range(1, 6)])

string_list = [str(num) for num in numbers]
print('string_list')
print(string_list)

# conditional logic with list comprehension
# if statement comes after for statement
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print('evens')
print(evens)
print('odds')
print(odds)

# if/else statement comes before for statement
doubled_evens_halved_odds = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]

print('doubled_evens_halved_odds')
print(doubled_evens_halved_odds)

# nested lists
board = [[num for num in range(1, 4)] for val in range(1, 4)]

print('board')
print(board)

x_and_o = [['X' if num % 2 != 0 else 'O' for num in range(1, 4)] for val in range(1, 4)]

print('x_and_o')
print(x_and_o)