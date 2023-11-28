user_input = input("Enter a string: ")


print("Original String is", user_input)
print("Printing only even index chars")

for index in range(0, len(user_input), 2):
    print(user_input[index])