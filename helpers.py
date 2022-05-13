import math
from math import sqrt
import time


def is_prime(whole_number):
    # Returns True if whole_number is prime and False if not prime
    divisor = 2

    if whole_number == 2:
        return True
    while whole_number % divisor !=0 and divisor < sqrt(whole_number):
        divisor += 1
    if divisor > sqrt(whole_number):
        return True
    else:
        return False


def is_prime_range(p, q):
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


def factorial(whole_number):
    # This solution begins with the number given then multiplies
    # by one less than the previous multiple
    accumulator = whole_number
    for multiple in range(whole_number - 1, 1, -1):
        accumulator *= multiple
    return accumulator


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


def is_sorted(list_of_elements, order):
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


def bubble_sort(list_of_items, order):
    # Function will return a given list in an ordered list either ascending or descending
    # The flag variable remains False until the list has finished sorting
    max_index = len(list_of_items) - 1
    passes = 0
    comparisons = 0
    swap = 0
    if order == "ascending" or order == "asc":
        sorted_flag = False
        while sorted_flag == False:
            index = 0
            sorted_flag = True
            while index < max_index:
                if list_of_items[index] > list_of_items[index + 1]:
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index + 1] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    sorted_flag = False
                    swap += 1
                comparisons +=1
                index += 1
            passes += 1
            max_index -= 1

    elif order == "descending" or order == "desc":
        sorted_flag = False
        while sorted_flag == False:
            index = 0
            sorted_flag = True
            while index < max_index:
                if list_of_items[index] < list_of_items[index + 1]:
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index + 1] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    sorted_flag = False
                index += 1
            max_index -= 1
    print(f'passes: {passes}, comparisons: {comparisons}, swaps {swap}')
    del passes, comparisons, swap
    return list_of_items


def new_bubble_sort(list):
    maximum_right_index = len(list) - 1
    minimum_left_index = 0
    comparisons = 0
    swap = 0
    back_and_forth = 0
    while minimum_left_index < maximum_right_index:
        index = minimum_left_index
        while index < maximum_right_index:
            if list[index] > list[index + 1]:
                list[index] = list[index] ^ list[index + 1]
                list[index + 1] = list[index] ^ list[index + 1]
                list[index] = list[index] ^ list[index + 1]
                swap += 1
            comparisons += 1
            index += 1

        maximum_right_index -= 1
        while index > minimum_left_index:
            if list[index] < list[index - 1]:
                list[index] = list[index] ^ list[index - 1]
                list[index - 1] = list[index] ^ list[index - 1]
                list[index] = list[index] ^ list[index - 1]
                swap += 1
            index -= 1
            comparisons += 1
        minimum_left_index += 1
        back_and_forth +=1
    print(f'back and forth: {back_and_forth}, comparisons: {comparisons}, swaps {swap}')
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


def transpose_matrix(matrix):
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


def merge(list_1, list_2, order):

    list_1_index = 0
    list_2_index = 0
    # this temp list will be used to return the final sorted list in this function
    temp_list_2 = []
    if order == 'desc':
        # the items in each list are being compared one by one and once
        # one of the indexes reaches its respective list's end then it exits
        while list_1_index < len(list_1) and list_2_index < len(list_2):
            if list_1[list_1_index] > list_2[list_2_index]:
                temp_list_2.append(list_1[list_1_index])
                list_1_index += 1
            else:
                temp_list_2.append(list_2[list_2_index])
                list_2_index += 1

        # this if statement will append all remaining items in the list that the index is not at the end
        if list_1_index == len(list_1):
            for element in list_2[list_2_index:]:
                temp_list_2.append(element)
        else:
            for element in list_1[list_1_index:]:
                temp_list_2.append(element)
    else:
        # the items in each list are being compared one by one and once
        # one of the indexes reaches its respective list's end then it exits
        while list_1_index < len(list_1) and list_2_index < len(list_2):
            if list_1[list_1_index] < list_2[list_2_index]:
                temp_list_2.append(list_1[list_1_index])
                list_1_index += 1
            else:
                temp_list_2.append(list_2[list_2_index])
                list_2_index += 1

        # this if statement will append all remaining items in the list that the index is not at the end
        if list_1_index == len(list_1):
            for element in list_2[list_2_index:]:
                temp_list_2.append(element)
        else:
            for element in list_1[list_1_index:]:
                temp_list_2.append(element)
    return temp_list_2


def merge_sort(input_list, order:str):
    temp_list = input_list[:]
    # these two assignment statements split the list in half
    temp_list_left = temp_list[:(len(temp_list) // 2)]
    temp_list_right = temp_list[(len(temp_list) // 2):]

    # If the left list has one element and the right list has more than one element
    # then the right list needs to be split further
    if len(temp_list_left) == 1 and len(temp_list_right) != 1:
        temp_list_right = merge_sort(temp_list_right, order)

    # If the right list has one element and the left list has more than one element
    # then the left list needs to be split further
    elif len(temp_list_left) != 1 and len(temp_list_right) == 1:
        temp_list_left = merge_sort(temp_list_left, order)

    # If both left and right lists have more than one element then both must be split
    elif len(temp_list_left) != 1 and len(temp_list_right) != 1:
        temp_list_left = merge_sort(temp_list_left, order)
        temp_list_right = merge_sort(temp_list_right, order)

    # Once all elements are split up into their smallest parts then this statement will run and
    # go back up the stack to return the result
    return merge(temp_list_left, temp_list_right, order)


def processing(text: str, wanted_characters: str):
    '''
    Removes all unwanted characters and excess spaces
    '''
    has_spaces = False
    # replaces unwanted characters and with a space
    for character in text:
        if character not in wanted_characters:
            text = text.replace(character, ' ')
        elif character == ' ':
            has_spaces = True
    # This loop removes all consecutive spaces
    if has_spaces:
        while True:
            max_spaces = 0
            current_max_spaces = 0
            for character_index in range(len(text) - 1):
                if text[character_index] != ' ' and text[character_index + 1] == ' ':
                    current_max_spaces = 1
                elif text[character_index] == ' ' and text[character_index + 1] == ' ':
                    current_max_spaces += 1
                else:
                    if current_max_spaces > max_spaces:
                        max_spaces = current_max_spaces
                    else:
                        current_max_spaces = 0
            if max_spaces % 2 == 0:
                text = text.replace('  ', ' ')
            elif max_spaces % 2 != 0 and max_spaces != 1:
                text = text.replace('   ', ' ')
            else:
                break
    return text


def find_bill_combos():
    """
    This function is for finding combinations of bills that add to a specific sum
    """
    wanted_characters = '0123456789. '
    bill_prices = input('Enter all bills to compare:\n')

    bill_prices = processing(bill_prices, wanted_characters)
    bill_list = bill_prices.split(' ')

    # This loop changes all the input into float data type for later comparison
    index = 0
    for item in bill_list:
        bill_list[index] = float(item)
        index += 1

    # we are sorting the list in descending order because we can infer information at certain points
    # that allow the function to have less iterations
    # bill_list_unordered = bill_list[:]
    bill_list = merge_sort(bill_list, order='desc')

    bill_sum = input('What is the sum you are looking for?\n')
    bill_sum = processing(bill_sum, wanted_characters)
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
        if max_sum > bill_sum > bill_list[starting_index]:
            # Assume there is a possible combination that starts with the starting index
            possible_combinations.append([bill_list[starting_index]])

            # the current_sum at this point starts with the current starting bill
            current_sum = bill_list[starting_index]

            # the second_starting_index is used to keep track of "inner" combinations with the starting_index bill
            second_starting_index = starting_index + 1
            while True:
                # if the current sum is less than the bill sum we can infer there is a possible combination that
                # includes the item currently being compared so add it to that combination and add it to the current sum
                if current_sum < bill_sum:
                    possible_combinations[-1].append(bill_list[compare_index])
                    current_sum += bill_list[compare_index]

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

                    # we have not reached the last element to compare with and we know there may still be a combination
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
        for item in possible_combinations:
            print(item)



if __name__ == "__main__":
    print(find_bill_combos())
    # M = [[1,2,3,4,5,6],[4,5,6,34,67],[7,8,9]]
    # print(print_column_row(M))
    # Mnew = M[:]
    # print(Mnew)
    # Msum =[]
    # for row in range(M):
    #     for col in row:
    #         Msum.insert(col,None)
    # print(Msum)

    # # Test Cases for find_min_max--------------------------------------------
    # if find_min_max([9, 33, 14, 5, 0], "min") == 0:
    #     print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))
    # else:
    #     print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "min"))
    #
    # if find_min_max([9, 33, 14, 5, 0], "max") == 33:
    #     print("Passed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))
    # else:
    #     print("Failed find_min_max", find_min_max([9, 33, 14, 5, 0], "max"))
    #
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
    # # Test Cases for factorial-------------------------------------------------
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
    # if factorial(0) == 0:
    #     print("Passed factorial")
    # else:
    #     print("Failed factorial", factorial(0))
    #
    # # Test cases for sort--------------------------------------------------
    # if bubble_sort([11, 5, 12, 6], "asc") == [5, 6, 11, 12]:
    #     print("Passed sort")
    # else:
    #     print("Failed sort", bubble_sort([11, 5, 12, 6], "asc"))
    # #
    # if bubble_sort([5, 4, 3, 2, 1], "asc") == [1, 2, 3, 4, 5]:
    #     print("Passed sort")
    # else:
    #     print("Failed sort", bubble_sort([5, 4, 3, 2, 1], "asc"))
    # print(bubble_sort([17,16,15,14,13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'asc'))
    # print(new_bubble_sort([17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))
    # print("End")
    # p = 1
    # q = 30
    # #[create a list of numbers]
    #
    # # L = [number for number in range(p, q+1) for divisor in range(2, int(sqrt(number))) if number]
    # #
    # # num_list = [number for number in [number for number in range(p, q+1)]]
    # # print(num_list)
    # # primes = [number for number in num_list if number == 1 or number == 2 or number == 3 for divisor in range(2, int(math.sqrt(number))+1) if number % divisor != 0 and divisor > math.sqrt(number)-1]
    # # print('primes', primes)
    # # print('is_prime_range function', is_prime_range(0,30))
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # list2 = [[item*item for item in row]for row in matrix]
    # list3 = [item*item for row in matrix for item in row]
    # list4 = [[row[i] for row in matrix] for i in range(len(matrix))]
    # list1 = [item*item for item in row for row in matrix]
    # print(list2)