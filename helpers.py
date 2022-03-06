from math import sqrt


def is_prime(whole_number):
    # Returns True if whole_number is prime and False if not prime
    divisor = 3

    if not isinstance(whole_number, int):
        raise TypeError("TypeError: Input must be a positive integer or zero")
    elif whole_number < 0:
        raise ValueError("ValueError: Negative numbers cannot be prime.")
    elif whole_number < 2 or whole_number % 2 == 0:
        return False
    else:
        while whole_number % divisor != 0 and divisor < sqrt(whole_number):
            divisor += 2
            if divisor % 5 == 0:
                divisor += 2
            print(divisor)
        if divisor >= sqrt(whole_number):
            return True
        else:
            return False


def sort(given_array, order):

    if len(given_array) == 0:
        return

x = "askljf"
try:
    int(x)
except Exception as e:
    print(e)
    # print("Variable x is a string and cannot be converted to an integer.")

#is_prime("k")
prime_test = 15877
# try:
#     is_prime(prime_test)
# except ValueError as v:
#     print(v)
# except TypeError as t:
#     print(t)

print(is_prime(prime_test))


print("End")