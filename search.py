# Searching algorithms implementations
import sorting
# import misc, so we can use the is_sorted function.


def linear_search_iterative(input_list, key):
    # each element in this list is being compared to the key
    for element in input_list:
        if element == key:
            return True
    return False


def linear_search_recursive(input_list, key):
    if len(input_list) == 0:
        return False
    elif input_list[0] == key:
        return True
    else:
        return linear_search_recursive(input_list[1:], key)


def binary_search_iterative(input_list, key):

    min_index = 0
    max_index = len(input_list) - 1

    if sorting.is_sorted(input_list, 'asc'):
        if key > input_list[max_index] or key < input_list[min_index]:
            return False
        else:
            while min_index <= max_index:
                mid_index = (min_index + max_index) // 2
                if key == input_list[mid_index]:
                    return True
                elif key > input_list[mid_index]:
                    min_index = mid_index + 1
                elif key < input_list[mid_index]:
                    max_index = mid_index - 1
            return False
    # else:
        # raise ValueError("List not sorted")


def binary_search_helper(input_list, key, min_index, mid_index, max_index):
    if min_index > max_index:
        return False
    elif key == input_list[mid_index]:
        return True
    elif key > input_list[mid_index]:
        return binary_search_helper(input_list, key, mid_index + 1, ((mid_index + 1) + max_index) // 2, max_index)
    else:
        return binary_search_helper(input_list, key, min_index, ((mid_index - 1) + min_index) // 2, mid_index - 1)



def binary_search_recursive(input_list, key):
    if key > input_list[-1] or key < input_list[0]:
        return False
    elif sorting.is_sorted(input_list, 'asc') == True:
        return binary_search_helper(input_list, key, 0, len(input_list) // 2, len(input_list) - 1)
   # else:
    #    raise ValueError("List is not sorted")


if __name__ == "__main__":
    L = [100, 86, 0, 4, 1, 27, 34, 3, 2, 97, 25, 9, 15, 99, 55]
    if linear_search_iterative(L, 99):
        print("Passed linear_search_iterative")
    else:
        print('Failed')

    if linear_search_recursive(L, 99):
        print("Passed linear_search_recursive")
    else:
        print('Failed linear_search_recursive')

    L = sorting.merge_sort(L, 'asc')

    if not binary_search_iterative(L, 85):
        print("Passed binary_search_iterative")
    else:
        print('Failed binary_search_iterative')

    if not binary_search_recursive(L, 85):
        print("Passed binary_search_recursive")
    else:
        print('Failed binary_search_recursive')
