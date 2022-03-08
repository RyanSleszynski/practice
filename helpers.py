from math import sqrt


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

def sort_using_min_max(list_of_items, order):
    # In this function, you are given a list of comparable objects/items such as numbers
    # Your job is to sort the items in ascending or descending order depending on the value of order
    # You have to make use of the find_max_min function that you have written above to implement this function.
    index = 0

    if order == "ascending" or order == "asc":
        acending = []
        while len(list_of_items) != 0:                         # each iteration passes a new list with the min removed
            minimum = find_max_min(list_of_items, "min")       # finds the min in the given list
            acending.insert(index, minimum)                    # adds the min to the new list
            list_of_items.remove(minimum)                      # removes the min from the given list
            index += 1
        return acending

    elif order == "descending" or order == "desc":
        decending = []
        while len(list_of_items) != 0:                         # same concept applied above to this loop as well
            maximum = find_max_min(list_of_items, "max")
            decending.insert(index, maximum)
            list_of_items.remove(maximum)
            index += 1
        return decending

    else:
        return "Invalid Request"

def is_sorted(list_of_elements, order):
    if order == "ascending" or order == "asc":
        index = 0
        while index < len(list_of_elements):
            if list_of_elements[index] > list_of_elements[index + 1]:
                return False
            else:
                return True

    if order == "descending" or order == "desc":
        index = 0
        while index < len(list_of_elements):
            if list_of_elements[index] < list_of_elements[index + 1]:
                return False
            else:
                return True


if __name__ == "__main__"
    print(is_sorted([1, 2, 3, 4, 5], "asc"))
    print(is_sorted([2, 5, 1 ,6], "desc"))
    print(is_sorted([6, 5, 2, 1], "desc"))

    # Test Cases for find_min_max
    if find_min_max([9, 33, 14, 5, 0], "min") == 0:
        print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))
    else:
        print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))

    if find_min_max([9, 33, 14, 5, 0], "max") == 33:
        print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))
    else:
        print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))

    # Test Cases for is_prime
    if is_prime(2):
        print("Passed is_prime(2)")
    else:
        print("Failed is_prime(2)")

    if not is_prime(25):
        print("Passed is_prime(25)")
    else:
        print("Failed is_prime(25)")