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


def find_min_max(list_of_items, min_or_max):
    # This function will return a minimum number or maximum number depending on the second argument
    # Errors will be raised if list_of_items is null or if min_or_max is NOT "min" or "max"
    # A for loop and a while loop are used to show possibility of either returning correct results

    index = 1

    if len(list_of_items) == 0:
        raise ValueError("Null set has no min or max")

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


def sort(list_of_items, order):
    # Function will return a given list in an ordered list either acending or decending
    # The flag variable remains False until the list has finished sorting

    flag = False
    while flag == False:
        for value in list_of_items:
             if value:

if find_min_max([9, 33, 14, 5, 0], "min") == 0:
    print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))
else:
    print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))

if find_min_max([9, 33, 14, 5, 0], "max") == 33:
    print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))
else:
    print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))


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