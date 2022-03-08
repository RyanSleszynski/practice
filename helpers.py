from math import *


def is_prime(whole_number):
    # Returns True if whole_number is prime and False if not prime
    divisor = 3

    # Checks for special cases and for simple input i.e. divisible by 2 or 5
    if whole_number < 2 or whole_number % 2 == 0 and whole_number != 2 or whole_number % 5 == 0:
        return False
    elif whole_number == 2:
        return True
    else:
        while not whole_number % divisor == 0 and divisor < sqrt(whole_number):
            divisor += 2
            print(divisor)
        if divisor >= sqrt(whole_number):
            return True
        else:
            return False

# Test Cases for is_prime
if is_prime(2):
    print("Passed is_prime(2)")
else:
    print("Failed is_prime(2)")

if not is_prime(25):
    print("Passed is_prime(25)")
else:
    print("Failed is_prime(25)")


def find_min_max(list_of_items, min_or_max):
    # This function will return a minimum number or maximum number depending on the second argument
    # Errors will be raised if list_of_items is null or if min_or_max is NOT "min" or "max"
    # A for loop and a while loop are used to show possibility of either returning correct results

    index = 1

    if len(list_of_items) == 0:
        print("Null set has no min or max")

    elif len(list_of_items) == 1:
        return list_of_items[0]

    elif min_or_max == "min":
        minimum = list_of_items[0]
        # For loop replaces the stored value of minimum if index_value is less than minimum
        for index_value in list_of_items:
            if minimum > index_value:
                minimum = index_value
        return minimum

        # While loop below replaces the stored value of minimum if list_of_items[index] is less than minimum
        # while index < len(list_of_items):
        #     if minimum > list_of_items[index]:
        #         minimum = list_of_items[index]
        #     index += 1
        # return minimum

    elif min_or_max == "max":
        maximum = list_of_items[0]
        while index < len(list_of_items):
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
    print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))
else:
    print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))

def sort(list_of_items, order):
    # Function will return a given list in an ordered list either acending or decending
    # The flag variable remains False until the list has finished sorting

    flag = False
    # while flag == False:
    #     for value in list_of_items:
    #          if value:




def sum(list_of_items):
    sum = 0
    for value in list_of_items:
        sum += value
    return sum

def factorial(whole_number):
    sum = 0
    accumulator = 1
    generate = whole_number
    while whole_number:
        sum = whole_number
        whole_number -= -1
print(sum([1,2,3,4,5,6]))

def sqroot(positive_integer):
    return positive_integer ** (1/2)

print(sqroot(4))