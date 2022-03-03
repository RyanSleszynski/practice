from math import *


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

def find_min_max(list_of_items, min_or_max):
    index = 0

    if len(list_of_items) == 0:
        raise ValueError("Null set has no min or max")

    elif min_or_max == "min":
        minimum = list_of_items[0]
        while index < len(list_of_items):
            if minimum > list_of_items[index]:
                minimum = list_of_items[index]
            index += 1
        return minimum

    elif min_or_max == "max":
        maximum = list_of_items[0]
        while index > len(list_of_items):
            if maximum < list_of_items[index]:
                maximum = list_of_items[index]
            index += 1
        return maximum

    else:
        raise ValueError("Second argument must be \"min\" or \"max\"")


if find_min_max([9, 33, 14, 5, 0], "min") == 0:
    print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))
else:
    print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))

if find_min_max([9, 33, 14, 5, 0], "max") == 33:
    print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))
else:
    print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))

def sort(given_array, order):

    if len(given_array) == 0:
        return
