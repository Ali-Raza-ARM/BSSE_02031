def calculate_result(number1, number2):
    product = number1 * number2

    if product <= 1000:
        return product
    else:
        return number1 + number2


number1_given1 = 20
number2_given1 = 30
result_given1 = calculate_result(number1_given1, number2_given1)
print(result_given1)


number1_given2 = 40
number2_given2 = 30
result_given2 = calculate_result(number1_given2, number2_given2)
print(result_given2)