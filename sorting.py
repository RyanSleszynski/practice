

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


def is_sorted(list_of_elements, order):
    # This function is faster than the is_sorted function which uses for loops instead of while
    # when the passed list is not sorted.
    if order == "ascending" or order == "asc":
        for item_index in range(len(list_of_elements)-1):
            if list_of_elements[item_index] > list_of_elements[item_index + 1]:
                return False
        return True

    elif order == "descending" or order == "desc":
        for item_index in range(len(list_of_elements) - 1):
            if list_of_elements[item_index] < list_of_elements[item_index + 1]:
                return False
        return True


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


def bubble_sort(list_of_items, order):
    # Function will return a given list in an ordered list either ascending or descending
    # The flag variable remains False until the list has finished sorting
    max_index = len(list_of_items) - 1
    if order == "ascending" or order == "asc":
        sorted_flag = False
        while sorted_flag is False:
            index = 0
            sorted_flag = True
            while index < max_index:
                if list_of_items[index] > list_of_items[index + 1]:
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index + 1] = list_of_items[index] ^ list_of_items[index + 1]
                    list_of_items[index] = list_of_items[index] ^ list_of_items[index + 1]
                    sorted_flag = False
                index += 1
            max_index -= 1

    elif order == "descending" or order == "desc":
        sorted_flag = False
        while sorted_flag is False:
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
    return list_of_items


def new_bubble_sort(list):
    """
    This function sorts through the passed argument in ascending order. The method is: bubble sort from left to right
    bringing the maximum value to the right then removing that from the comparisons because we know it is the greatest
    then go from right to left moving the minimum value to the left then removing that from the comparisons because we
    know it is the minimum


    :param list: a list of items
    :return: a sorted list in ascending order

    """
    maximum_right_index = len(list) - 1
    minimum_left_index = 0
    while minimum_left_index < maximum_right_index:
        index = minimum_left_index
        while index < maximum_right_index:
            if list[index] > list[index + 1]:
                list[index] = list[index] ^ list[index + 1]
                list[index + 1] = list[index] ^ list[index + 1]
                list[index] = list[index] ^ list[index + 1]
            index += 1

        maximum_right_index -= 1
        while index > minimum_left_index:
            if list[index] < list[index - 1]:
                list[index] = list[index] ^ list[index - 1]
                list[index - 1] = list[index] ^ list[index - 1]
                list[index] = list[index] ^ list[index - 1]
            index -= 1
        minimum_left_index += 1
    return list


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


def merge_sort(input_list, order: str):
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


def selection_sort(input_list):
    temp_list = input_list[:]

    # next_minimum_index represents the index of the item that is going to be the next minimum once
    # that minimum is found
    next_minimum_index = 0

    # While the next_minimum_index is less than the length of the list then the list is not necessarily sorted yet
    while next_minimum_index < len(temp_list):
        # While it is not sorted. Find the next minimum that is greater than the greatest known minimum
        # We assume the minimum is the next element being considered
        minimum_index = next_minimum_index
        # The assumed minimum_index is compared to the element immediately after it
        compare_index = minimum_index + 1

        # We compare the value at minimum_index to all values to the right of it to find the index of the next minimum
        while compare_index < len(temp_list):
            if temp_list[minimum_index] > temp_list[compare_index]:
                minimum_index = compare_index
            compare_index += 1

        # If the next minimum element is already in the position it needs to be it does not swap
        # otherwise it does swap
        if minimum_index != next_minimum_index:
            temp_list[next_minimum_index] = temp_list[minimum_index] ^ temp_list[next_minimum_index]
            temp_list[minimum_index] = temp_list[minimum_index] ^ temp_list[next_minimum_index]
            temp_list[next_minimum_index] = temp_list[minimum_index] ^ temp_list[next_minimum_index]
        next_minimum_index += 1
    return temp_list


def insertion_sort(input_list):

    temp_list = input_list[:]

    # Optimized solution below -------------------------------------------------------------------
    # The next_element_index represents the item in the list that is being considered
    next_element_index = 1
    # When next_element_index is one greater than the length of the list then the list is sorted
    while next_element_index < len(temp_list):
        # index represents the element being considered but will keep track of the number as
        # it moves down the list to where it belongs
        index = next_element_index
        # While the number before the index is greater than the element at index it will swap them
        while temp_list[index - 1] > temp_list[index] and index > 0:
            temp_list[index] = temp_list[index] ^ temp_list[index - 1]
            temp_list[index - 1] = temp_list[index] ^ temp_list[index - 1]
            temp_list[index] = temp_list[index] ^ temp_list[index - 1]
            index -= 1
        next_element_index += 1
    return temp_list


def counting_sort(input_list):
    original_list = input_list[:]
    count_list = []
    temp_list = input_list[:]
    maximum_value = 0

    # This finds the maximum value in the list, so we know how many indexes we need in the count_list
    for element in original_list:
        if element > maximum_value:
            maximum_value = element

    # This creates the proper number of indexes in count_list
    while maximum_value >= 0:
        count_list.append(0)
        maximum_value -= 1

    considered_element_index = 0
    compare_index = 1

    # Finds how many of the considered_element is in the list
    while considered_element_index < len(original_list):  # May give an index error
        if count_list[original_list[considered_element_index]] == 0:
            count_of_considered_element = 1
            while compare_index < len(original_list):

                if original_list[considered_element_index] == original_list[compare_index]:
                    count_of_considered_element += 1
                compare_index += 1

            count_list[original_list[considered_element_index]] = count_of_considered_element

        considered_element_index += 1
        compare_index = considered_element_index + 1

    # This loop gets us the indexes of the values in the temp_list
    count_index = 0
    while count_index < len(count_list) - 1:
        count_list[count_index + 1] = count_list[count_index] + count_list[count_index + 1]
        count_index += 1

    considered_element_index = 0
    while considered_element_index < len(original_list):
        temp_list[count_list[original_list[considered_element_index]] - 1] = original_list[considered_element_index]
        count_list[original_list[considered_element_index]] -= 1
        considered_element_index += 1

    return temp_list


if __name__ == "__main__":
    print(find_min_max([1,6,78,1,5], 'min'))