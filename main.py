import strings_dictionaries
import sorting
import mathematics


# wanted_characters = '0123456789. '
#
# numbers = input('Enter each number separated by a space or comma:\n')
# numbers = strings_dictionaries.preprocessing(numbers, wanted_characters)
# number_list = numbers.split()
#
# print(number_list)
#
# # This loop changes all the input into float data type for later comparison
# index = 0
# for item in number_list:
#     number_list[index] = float(item)
#     index += 1
# del item, numbers
# # we are sorting the list in descending order because we can infer information at certain points
# # that allow the function to have fewer iterations
# # bill_list_unordered = number_list[:]
# if len(number_list) >= 2:
#     number_list = sorting.merge_sort(number_list, order='desc')
# else:
#     raise ValueError('Must have more than one item in the list.')
# print('sorted list', number_list)
# wanted_sum = input('What is the sum you are looking for?\n')
# wanted_sum = strings_dictionaries.preprocessing(wanted_sum, wanted_characters)
# wanted_sum = float(wanted_sum)
