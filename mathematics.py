import math
from math import sqrt
import strings_dictionaries
import sorting
import time


def is_prime(whole_number: int):
    """
    Returns whether a given number is prime

    :param whole_number: positive integer
    :return: Boolean
    """
    # Returns True if whole_number is prime and False if not prime
    divisor = 2

    if whole_number == 2:
        return True
    while whole_number % divisor != 0 and divisor < sqrt(whole_number):
        divisor += 1
    if divisor > sqrt(whole_number):
        return True
    else:
        return False


def is_prime_range(p, q):
    """
    Returns all the prime numbers in a range of numbers

    :param p: positive integer less than q
    :param q: positive integer greater than p
    :return: list of integers
    """
    result = []
    for number in range(p, q + 1):
        for divisor in range(2, int(math.sqrt(number))+1):
            if number % divisor == 0:
                break
            elif divisor > math.sqrt(number)-1:
                result.append(number)

    return result


def my_sum(list_of_items):
    accumulator = 0
    for value in list_of_items:
        accumulator += value
    return accumulator


def factorial(whole_number: int):
    """
    Returns the factorial calculation of a given number

    :param whole_number: a positive integer or zero
    :return: integer
    """
    # Special case
    if whole_number == 0:
        return 1

    # This solution begins with the number given then multiplies
    # by one less than the previous multiple
    accumulator = whole_number
    for multiple in range(whole_number - 1, 1, -1):
        accumulator *= multiple
    return accumulator


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


def find_combos(iterable, method, wanted_sum):
    """
    This function finds combinations of numbers that add to a specific sum.
    """
    combo_dict = {}

    def get_combos():
        counter = 0
        for item_index in range(len(iterable)-1, -1, -1):
            counter += 1
            if len(combo_dict) >= 1:
                temp = []
                # This loop takes all previous entries and adds them to the current entry for later processing
                for key, value in combo_dict.items():
                    counter += 1
                    for combo in value:
                        counter += 1
                        temp.append(tuple(list(combo) + [iterable[item_index]]))
                combo_dict[iterable[item_index]] = [(iterable[item_index],)] + temp
            else:
                combo_dict[iterable[item_index]] = [(iterable[item_index],)]
        print('iterations:', counter)

    if method == 'sum':
        get_combos()
        possible_combinations = []
        for value in combo_dict.values():
            for combo in value:
                if sum(combo) == wanted_sum:
                    possible_combinations.append(combo)
        if len(possible_combinations) == 0:
            return False, 'Sorry we couldn\'t find any combinations.'
        else:
            return True, possible_combinations
    return combo_dict

if __name__ == "__main__":
    input = [111,100,96,54,32,21,17,12,5,3,2,1]
    start = time.time()
    input_combos = find_combos(input,'sum', 118)
    end = time.time()
    print(f'Time taken: {(end - start) * 100}')
    print(input_combos[1])

    # # Test Cases for is_prime-------------------------------------------------
    # if not is_prime(9):
    #     print("Passed is_prime(9)")
    # else:
    #     print("Failed is_prime(9)")
    #
    # if is_prime(113):
    #     print("Passed is_prime(113)")
    # else:
    #     print("Failed is_prime(113)")
    #
    # Test Cases for factorial-------------------------------------------------
    # if factorial(3) == 6:
    #     print("Passed factorial")
    # else:
    #     print("Failed factorial", factorial(3))
    #
    # if factorial(5) == 120:
    #     print("Passed factorial")
    # else:
    #     print("Failed factorial", factorial(5))
    #
    # if factorial(7) == 5040:
    #     print("Passed factorial")
    # else:
    #     print("Failed factorial", factorial(7))
    #
    # if factorial(1) == 1:
    #     print("Passed factorial")
    # else:
    #     print("Failed factorial", factorial(1))
    #
    # if factorial(0) == 1:
    #     print("Passed factorial")
    # else:
    #     print("Failed factorial", factorial(0))
