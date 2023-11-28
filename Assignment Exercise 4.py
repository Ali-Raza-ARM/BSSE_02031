def check_first_last_equal(numbers):
    result = numbers[0] == numbers[-1]
    return result

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

result_x = check_first_last_equal(numbers_x)
result_y = check_first_last_equal(numbers_y)

print(f"Given list: {numbers_x} result is {result_x}")
print(f"Given list: {numbers_y} result is {result_y}")