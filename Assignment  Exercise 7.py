
def is_palindrome(number):
   
    num_str = str(number)
    
   
    return num_str == num_str[::-1]


num1 = 121
num2 = 125


print("original number", num1)
if is_palindrome(num1):
    print("Yes. Given number is a palindrome number")
else:
    print("No. Given number is not a palindrome number")

print("\noriginal number", num2)
if is_palindrome(num2):
    print("Yes. Given number is a palindrome number")
else:
    print("No. Given number is not a palindrome number")