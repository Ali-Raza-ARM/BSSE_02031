print("Printing current and previous number sum in a range (10)")

previous_number = 0

for current_number in range(10):
    current_sum = current_number + previous_number
    print(f"Current Number {current_number} & Previous Number {previous_number} Sum: {current_sum}")
    previous_number = current_number