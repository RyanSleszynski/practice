from math import sqrt
import time


def wait(seconds=0):
    waiting = True
    current_time = time.time()
    while waiting:
        new_time = time.time()
        if new_time >= current_time + seconds:
            waiting = False
        new_time = time.time()



def is_prime(whole_number):
    # Returns True if whole_number is prime and False if not prime
    divisor = 3

    if whole_number < 2 or whole_number % 2 == 0 and whole_number != 2 or whole_number % 5 == 0:
        return False
    elif whole_number == 2:
        return True
    else:
        while whole_number % divisor != 0 and divisor < sqrt(whole_number):
            divisor += 2
            if divisor % 5 == 0:
                divisor += 2
        if divisor > sqrt(whole_number):
            return True
        else:
            return False


def my_sum(list_of_items):
    accumulator = 0
    for value in list_of_items:
        accumulator += value
    return accumulator


def factorial(whole_number):
    # This solution begins with the number given then multiplies
    # by one less than the previous multiple
    accumulator = whole_number
    for multiple in range(whole_number - 1, 1, -1):
        accumulator *= multiple
    return accumulator


def bubble_sort(list_of_items, order):
    # Function will return a given list in an ordered list either ascending or descending
    # The flag variable remains False until the list has finished sorting
    if order == "ascending" or order == "asc":
        sorted_flag = False
        while sorted_flag == False:
            index = 0
            change_counter = 0
            while index < len(list_of_items) - 1:
                if list_of_items[index] > list_of_items[index + 1]:
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index + 1] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    change_counter += 1
                index += 1
            if change_counter == 0:
                sorted_flag = True

    elif order == "descending" or order == "desc":
        sorted_flag = False
        while sorted_flag == False:
            index = 0
            change_counter = 0
            while index < len(list_of_items) - 1:
                if list_of_items[index] < list_of_items[index + 1]:
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index + 1] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    change_counter += 1
                index += 1
            if change_counter == 0:
                sorted_flag = True
    return list_of_items


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

    elif min_or_max == "max":
        maximum = list_of_items[0]
        for index_value in list_of_items:
            if maximum < index_value:
                maximum = index_value
            index += 1
        return maximum

    else:
        raise ValueError("Second argument must be \"min\" or \"max\"")


def sort_using_min_max(list_of_items, order):
    # This function is about 22 times faster on average than the sort function
    # This function takes the maximum or minimum in a list then adds it to a new list to be returned
    # when the original passed list is empty
    index = 0
    if order == "ascending" or order == "asc":
        ascending = []
        while len(list_of_items) != 0:                         # each iteration passes a new list with the min removed
            minimum = find_min_max(list_of_items, "min")       # finds the min in the given list
            ascending.insert(index, minimum)                    # adds the min to the new list
            list_of_items.remove(minimum)                      # removes the min from the given list
            index += 1
        return ascending

    elif order == "descending" or order == "desc":
        descending = []
        while len(list_of_items) != 0:                         # same concept applied above to this loop as well
            maximum = find_min_max(list_of_items, "max")
            descending.insert(index, maximum)
            list_of_items.remove(maximum)
            index += 1
        return descending

    else:
        raise ValueError("order parameter must be asc or desc")


def is_sorted_while(list_of_elements, order):
    # This function is faster than the is_sorted function which uses for loops instead of while
    # when the passed list is not sorted.
    if order == "ascending" or order == "asc":
        index = 0
        while index < len(list_of_elements) - 1:
            if list_of_elements[index] > list_of_elements[index + 1]:
                return False
            else:
                index += 1
        return True

    elif order == "descending" or order == "desc":
        index = 0
        while index < len(list_of_elements) - 1:
            if list_of_elements[index] < list_of_elements[index + 1]:
                return False
            else:
                index += 1
        return True


def is_sorted(list_of_elements, order):
    # This function using for loops is significantly faster than using a while loop if the list is sorted
    # However it is slower than using a while loop if the list is unsorted because the for loop
    # creates an identical list with the first element missing to compare values
    # This also uses more space than the while loop because it holds two lists in memory
    if order == "ascending" or order == "asc":
        comparing_list = list_of_elements[1:]
        for first, second in zip(list_of_elements, comparing_list):
            if first > second:
                return False
        return True

    if order == "descending" or order == "desc":
        comparing_list = list_of_elements[1:]
        for first, second in zip(list_of_elements, comparing_list):
            if first < second:
                return False
        return True


def new_bubble_sort(list):
    maximum_right_index = len(list) - 1
    while not is_sorted_while(list, "asc") and maximum_right_index != 0:
        left_index = 0
        right_index =1
        while right_index <= maximum_right_index:
            if list[left_index] > list[right_index]:
                list[left_index] = list[left_index] ^ list[right_index]
                list[right_index] = list[left_index] ^ list[right_index]
                list[left_index] = list[left_index] ^ list[right_index]
            left_index += 1
            right_index += 1
        maximum_right_index -= 1
    return list


def combinations(list):
    original_list = list[:]
    temp_list = original_list[:]
    list_size = len(list)
    print(original_list)
    combination_count = 1
    while list_size >= 0:
        ignored_index = 0
        while ignored_index < len(temp_list):
            print(temp_list[0:ignored_index] + temp_list[ignored_index+1:])
            ignored_index += 1
            combination_count += 1
    pass

def rotate_90_matrix(matrix):
    row_index = 0
    while row_index < len(matrix):
        column_index = 0
        while column_index <= row_index:
            matrix[row_index][column_index] = matrix[row_index][column_index] ^ matrix[column_index][row_index]
            matrix[column_index][row_index] = matrix[row_index][column_index] ^ matrix[column_index][row_index]
            matrix[row_index][column_index] = matrix[row_index][column_index] ^ matrix[column_index][row_index]
            column_index += 1
        row_index += 1
    return matrix

def print_column_row(matrix):

    column = 0
    maximum_row_length = 0
    for item in matrix:
        if len(item) > maximum_row_length:
            maximum_row_length = len(item)

    while column < maximum_row_length:
        row = 0
        while row < len(matrix):
            if column < len(matrix[row]):
                print(matrix[row][column])
            row += 1
        column += 1


def monty_carlo(a, b, c, d):
    if a < b:
        if (a < c < b and not a < d < b) or (a < d < b and not a < c < b):
            return True
        else:
            return False
    elif b < a:
        if (b < c < a and not b < d < a) or (b < d < a and not b < c < a):
            return True
        else:
            return False
    else:
        raise ValueError('These input does not create a line.')


if __name__ == "__main__":
    M = [[1,2,3,4,5,6],[4,5,6,34,67],[7,8,9]]
    print(print_column_row(M))
    Mnew = M[:]
    print(Mnew)
    # Msum =[]
    # for row in range(M):
    #     for col in row:
    #         Msum.insert(col,None)
    # print(Msum)

    # Test Cases for find_min_max--------------------------------------------
    if find_min_max([9, 33, 14, 5, 0], "min") == 0:
        print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))
    else:
        print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))

    if find_min_max([9, 33, 14, 5, 0], "max") == 33:
        print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))
    else:
        print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))

    # Test Cases for is_prime-------------------------------------------------
    if not is_prime(9):
        print("Passed is_prime(2)")
    else:
        print("Failed is_prime(2)")

    if is_prime(113):
        print("Passed is_prime(25)")
    else:
        print("Failed is_prime(25)")

    # Test Cases for factorial-------------------------------------------------
    if factorial(3) == 6:
        print("Passed factorial")
    else:
        print("Failed factorial", factorial(3))

    if factorial(5) == 120:
        print("Passed factorial")
    else:
        print("Failed factorial", factorial(5))

    if factorial(7) == 5040:
        print("Passed factorial")
    else:
        print("Failed factorial", factorial(7))

    if factorial(1) == 1:
        print("Passed factorial")
    else:
        print("Failed factorial", factorial(1))

    if factorial(0) == 0:
        print("Passed factorial")
    else:
        print("Failed factorial", factorial(0))

    # Test cases for sort--------------------------------------------------
    if bubble_sort([11, 5, 12, 6], "asc") == [5, 6, 11, 12]:
        print("Passed sort")
    else:
        print("Failed sort", bubble_sort([11, 5, 12, 6], "asc"))

    if bubble_sort([5, 4, 3, 2, 1], "asc") == [1, 2, 3, 4, 5]:
        print("Passed sort")
    else:
        print("Failed sort", bubble_sort([5, 4, 3, 2, 1], "asc"))

    print(new_bubble_sort([2,1,23,4,7,6,40]))
    print("End")