import math
from math import sqrt
import strings_dictionaries
import sorting
import time
import sys


def is_prime(whole_number: int):
    """
    Returns whether a given number is prime

    :param whole_number: positive integer
    :return: True if whole_number is prime, False if whole_number is NOT prime
    """

    if whole_number < 0:
        raise ValueError('ValueError: argument should be non-negative.')
    for divisor in range(2, sqrt(whole_number).__floor__() + 1):
        if whole_number % divisor == 0:
            return False
    return True


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


def combinations():
    pass


def get_combos(iterable):
    """
    Gets all possible combinations of an iterable using iteration.

    Method description -- Starting with the last item in the iterable a single combination is made and all
    subsequent combinations are based on all previously calculated combinations

    :param iterable: iterable object
    :return: a dictionary(hash table) of all possible combinations
    """
    combo_dict = {iterable[-1]: [(iterable[-1],)]}
    for item_index in range(len(iterable)-2, -1, -1):
        # This loop takes all previous entries and adds them to the current entry for later processing
        # we are appending a tuple because of a problem with mutability of lists.
        combo_dict[iterable[item_index]] = [(iterable[item_index],)] + [tuple(list(combo) + [iterable[item_index]]) for value in combo_dict.values() for combo in value]

    return combo_dict


def combo_sums(combo_dict, wanted_sum):
    """
    Finds combinations that sum to a given number

    :param  combo_dict: a dictionary of combinations where key=a value in the original iterable
        value=two-dimensional iterable
    :param  wanted_sum: a number you want the combinations to sum to

    :returns: list of tuples
    """
    possible_combinations = [combo for value in combo_dict.values() for combo in value if sum(combo) == wanted_sum]

    return possible_combinations


if __name__ == "__main__":
    input = [120,117,114,110, 108, 106, 104,100,96,54,32,21,17,12,5,3,2,1]
    print(f'Number of items: {len(input)}')

    start = time.time()
    input_combos = get_combos(input)
    end = time.time()
    print(f'Time taken to generate all combinations: {(end - start)} seconds')

    start = time.time()
    input_combo_sum = combo_sums(input_combos, 15)
    end = time.time()
    print(f'Time taken to find sums: {(end - start)} seconds')

    for combo_num, combo in enumerate(input_combo_sum, start=1):
        print(f'Combination number {combo_num}: {combo}')

    # # Test Cases for is_prime-------------------------------------------------
    # if not is_prime(9):
    #     print("Passed is_prime(9)")
    # else:
    #     print("Failed is_prime(9)")
    #
    # if is_prime(2):
    #     print("Passed is_prime(2)")
    # else:
    #     print("Failed is_prime(2)")
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
