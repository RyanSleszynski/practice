# This program will be able to determine if a given number input is a prime number or not
print("Welcome to the Prime Number Program. The program will tell you if a number you give is a prime number or not.")
#input("Press any key to continue.")

number_1 = int(input("Enter the number you wish to check: "))
count: int = 1

while (number_1 % (count + 2) != 0) and (count + 2) < number_1 and number_1 % 2 != 0 and number_1 % 5 != 0:
    count = count + 2
    print(count)
if count + 2 == number_1:
    print("The number you entered is a prime number.")
else:
    print("The number you entered is not a prime number.")
