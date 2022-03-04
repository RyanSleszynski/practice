from math import sqrt


def is_prime(whole_number):
    # Returns True if whole_number is prime and False if not prime
    divisor = 3

    if whole_number < 2 or whole_number % 2 == 0:
        return False
    else:
        while whole_number % divisor != 0 and divisor < sqrt(whole_number):
            divisor += 2
            print(divisor)
        if divisor >= sqrt(whole_number):
            return True
        else:
            return False


def sort(given_array, order):

    if len(given_array) == 0:
        return
