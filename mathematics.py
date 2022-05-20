import math
from math import sqrt
import strings_dictionaries
import sorting


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


def find_bill_combos():
    """
    This function finds combinations of numbers that add to a specific sum. Input handling is included in the function
    """
    wanted_characters = '0123456789. '
    bill_list = []
    bill_index = 0
    bill_price = input(f'Enter one bill price at a time:\n{bill_index + 1}: ')
    while bill_price != '':
        bill_price = strings_dictionaries.preprocessing(bill_price, wanted_characters)
        bill_list.append(bill_price)
        bill_index += 1
        bill_price = input(f'{bill_index + 1}: ')

    print(bill_list)

    # This loop changes all the input into float data type for later comparison
    index = 0
    for item in bill_list:
        bill_list[index] = float(item)
        index += 1
    del item, bill_price
    # we are sorting the list in descending order because we can infer information at certain points
    # that allow the function to have fewer iterations
    # bill_list_unordered = bill_list[:]
    if len(bill_list) >= 2:
        bill_list = sorting.merge_sort(bill_list, order='desc')
    else:
        raise ValueError('Must have more than one item in the list.')
    print('sorted list', bill_list)
    bill_sum = input('What is the sum you are looking for?\n')
    bill_sum = strings_dictionaries.preprocessing(bill_sum, wanted_characters)
    bill_sum = float(bill_sum)

    possible_combinations = []
    starting_index = 0

    # Combination checking loop
    while starting_index < len(bill_list):
        compare_index = starting_index + 1

        # here we are getting the maximum possible sum from the starting bill to the lowest bill
        max_sum = bill_list[starting_index]
        while compare_index < len(bill_list):
            max_sum = max_sum + bill_list[compare_index]
            compare_index += 1
        compare_index = starting_index + 1

        # if it is possible for the bills to sum to bill_sum, then we check further
        if max_sum > bill_sum >= bill_list[starting_index]:
            # Assume there is a possible combination that starts with the starting index
            possible_combinations.append([bill_list[starting_index]])

            # the current_sum at this point starts with the current starting bill
            current_sum = bill_list[starting_index]

            # the second_starting_index is used to keep track of "inner" combinations with the starting_index bill
            second_starting_index = starting_index + 1
            while True:
                # if the current_sum is less than the bill_sum, and we are comparing with the last
                # element then that combination will not sum to bill sum, so
                # we can remove that combination
                if current_sum < bill_sum and compare_index == len(bill_list)-1:
                    possible_combinations = possible_combinations[:-1]
                    break

                # if the current sum is less than the bill sum we can infer there is a possible combination that
                # includes the item currently being compared so add it to that combination and add it to the current sum
                elif current_sum < bill_sum and compare_index != len(bill_list)-1:
                    possible_combinations[-1].append(bill_list[compare_index])
                    current_sum += bill_list[compare_index]
                    # compare_index += 1

                # if the current_sum is greater than the bill_sum there may still be a combination
                elif current_sum > bill_sum:

                    # if we reached the last element in the bill list then there are no more elements to compare with
                    # therefore we should remove that entire combination and start a new combination with
                    # the next "inner" index
                    if compare_index == len(bill_list):
                        possible_combinations = possible_combinations[:-1]
                        possible_combinations.append([bill_list[starting_index], bill_list[second_starting_index]])
                        current_sum = bill_list[starting_index] + bill_list[second_starting_index]
                        second_starting_index += 1
                        compare_index = second_starting_index + 1

                        # find the maximum value of the elements that come after the second_starting_index
                        current_max = 0
                        for item in bill_list[second_starting_index:]:
                            current_max += item

                        # if that sum is less than the wanted sum then there can be no more possibilities
                        # with this starting_index
                        if bill_list[starting_index] + current_max < bill_sum:
                            break

                    # we have not reached the last element to compare with, and we know there may still be a combination
                    # excluding the current compared element. therefore, remove that element from the sum and the combination
                    # compare with the next number and add it to the combination and the sum
                    else:
                        current_sum -= bill_list[compare_index]
                        possible_combinations[-1].remove(bill_list[compare_index])
                        compare_index += 1
                        possible_combinations[-1].append(bill_list[compare_index])
                        current_sum += bill_list[compare_index]
                else:
                    break

        # if the sum of all bills less than the starting bill equals the sum then that is
        # the last possible combination add it then break out of loop
        elif max_sum == bill_sum:
            possible_combinations.append([])
            for item in bill_list[starting_index:]:
                possible_combinations[-1].append(item)
            break

        # at any point when the max_sum for that particular iteration is less than the wanted sum
        # we can infer that there are no more possible combinations
        elif max_sum < bill_sum:
            break
        starting_index += 1

    if len(possible_combinations) == 0:
        print('Sorry but we could not find any combinations of the bills you entered.')
    else:
        print('Here are all possible combinations:')
        for item in possible_combinations:
            print(item)


if __name__ == "__main__":
    find_bill_combos()
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
