from math import sqrt
# This program will be able to determine if a given number input is a prime number or not
print("Welcome to the Prime Number Program. The program will tell you if a number you give is a prime number or not.")
# input("Press any key to continue.")

num_1 = input("Enter the number you wish to check: ")
divisor: int = 3

while num_1 < 0 or type(num_1) == int:

while num_1 % divisor != 0 and divisor < num_1 and num_1 % 2 != 0 and num_1 % 5 != 0:
    divisor = divisor + 2
    if divisor % 5 == 0:
        divisor = divisor + 2
    print(divisor)

if divisor == num_1:
    print("The number you entered is a prime number.")
else:
    print("The number you entered is not a prime number.")
