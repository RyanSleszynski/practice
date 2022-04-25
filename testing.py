import random
import time
import helpers
import helpers_recursive


# def instance_input(data_type, data_type_2=""):
#     max_value = 100
#     # Setting the seed to make sure that the same random list is generated every time with the same parameters
#     random.seed(124)
#     number_of_trials = 5000
#     if data_type == "int":
#         return [int(random.random() * max_value) for i in range(number_of_trials)]
#     elif data_type == "list" and data_type_2 == "int":
#         return [[int(random.random() * max_value) for i in range(number_of_trials)] for i in range(number_of_trials)]
#     elif data_type == "str" and data_type_2 == "order":
#         return [random.choice(["asc", "desc"]) for i in range(number_of_trials)]
#
#
# def time_test(file_name, function_name):
#     number_of_trials = 10  # you can change this number to make the testing faster.
#     number_of_trials_per_input = 10
#
#     if file_name == "helpers" and function_name == "is_prime":
#
#
#         print("Instancing input...")
#         input_list = instance_input("int")
#         print("Input instanced.")
#         print(function_name, "time trials start:")
#
#         total_time_taken = 0
#         for item in input_list:  # run for all the input
#             total_time_taken_current_trial = 0
#             for trial in range(number_of_trials_per_input):  # now run multiple times for every input
#                 start_time = time.time()
#                 helpers.is_prime(item)
#                 end_time = time.time()
#                 time_taken_current_trial = end_time - start_time
#                 total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
#             total_time_taken = total_time_taken + total_time_taken_current_trial
#         print('Average time taken by', str(function_name) + ":", total_time_taken / number_of_trials)
#         return print(function_name, "time trials end.")
#
#     elif file_name == "helpers" and function_name == "my_sum":
#         print("Instancing input...")
#         input_list = instance_input("list", "int")
#         print("Input instanced.")
#         print(function_name, "time trials start:")
#
#         total_time_taken = 0
#         for item in input_list:  # run for all the input
#             total_time_taken_current_trial = 0
#             for trial in range(number_of_trials_per_input):  # now run multiple times for every input
#                 start_time = time.time()
#                 helpers.my_sum(item)
#                 end_time = time.time()
#                 time_taken_current_trial = end_time - start_time
#                 total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
#             total_time_taken = total_time_taken + total_time_taken_current_trial
#         print('Average time taken by', str(function_name) + ":", total_time_taken / number_of_trials)
#         return print(function_name, "time trials end.")
#
#     elif file_name == "helpers" and function_name == "sort":
#         print("Instancing input...")
#         input_list = instance_input("list", "int")
#         input_list_order = [random.choice(["asc", "desc"]) for i in range(number_of_trials)]
#         print("Input instanced.")
#         print(function_name, "time trials with random lists start:")
#
#         total_time_taken = 0
#         for item_list, item_order in zip(input_list, input_list_order):  # run for all the input
#             total_time_taken_current_trial = 0
#             for trial in range(number_of_trials_per_input):  # now run multiple times for every input
#                 start_time = time.time()
#                 helpers.sort(item_list, item_order)
#                 end_time = time.time()
#                 time_taken_current_trial = end_time - start_time
#                 total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
#             total_time_taken = total_time_taken + total_time_taken_current_trial
#
#         print('Average time taken by', str(function_name) + ":", total_time_taken / number_of_trials)
#
#     elif file_name == "helpers" and function_name == "sort_using_min_max":
#         print("Instancing input...")
#         input_list = instance_input("list", "int")
#         input_list_order = [random.choice(["asc", "desc"]) for i in range(number_of_trials)]
#         print("Input instanced.")
#         print(function_name, "time trials with random lists start:")
#
#         total_time_taken = 0
#         for item_list, item_order in zip(input_list, input_list_order):  # run for all the input
#             total_time_taken_current_trial = 0
#             for trial in range(number_of_trials_per_input):  # now run multiple times for every input
#                 start_time = time.time()
#                 helpers.sort_using_min_max(item_list, item_order)
#                 end_time = time.time()
#                 time_taken_current_trial = end_time - start_time
#                 total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
#             total_time_taken = total_time_taken + total_time_taken_current_trial
#
#         print('Average time taken by', str(function_name) + ":", total_time_taken / number_of_trials)


def first_point_generation(number_of_trials=10000):
    a, b = 0, 360
    first_point_input = []
    for trial in range(number_of_trials):
        first_point = random.randrange(a, b)
        first_point_input.append(first_point)
    return first_point_input


def second_point_generation(first_point_input: list, number_of_trials=10000):
    a, b = 0, 360
    first_point_index = 0
    second_point_input = []
    for trial in range(number_of_trials):
        second_point = random.randint(a, b)
        while first_point_input[first_point_index] == second_point:
            second_point = random.randint(a, b)
        second_point_input.append(second_point)
        first_point_index += 1
    return second_point_input


def does_intersect(a, b, c, d):
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
        raise ValueError('The input does not create a line.')


# All values are based on degrees. For example: a value of 180 would assume a point 180 degrees from any designated 0
# If a point from segment ab and cd are equal they are considered to NOT intersect
# input for the second point of each line segment is based on the respective first point
# This was done because of the assumption that if a = b then there is an error because it
# does not create a line. To get around this, if the randomly picked second point
# equals the first point for that respective pair then the second point is randomized again until a != b

random.seed()
number_of_trials = 1_000_000


print('Creating input for point \"a\"')
a_input = first_point_generation(number_of_trials)

print('Creating input for point \"b\"')
b_input = second_point_generation(a_input, number_of_trials)

print('Creating input for point \"c\"')
c_input = first_point_generation(number_of_trials)

print('Creating input for point \"d\"')
d_input = second_point_generation(c_input, number_of_trials)

print('Zipping all input')
input_list = list(zip(a_input, b_input, c_input, d_input))
print('End of zip')

results = {'intersect': 0,
           'non-intersect': 0}

# result_truth was created to confirm correct answers
result_truth = []
print('Start of Trials:')
for trial in input_list:
    current_trial_result = does_intersect(trial[0], trial[1], trial[2], trial[3])
    result_truth.append(current_trial_result)
    if current_trial_result:
        results['intersect'] += 1
    else:
        results['non-intersect'] += 1
print('End of Trials')
print('Percentage of intersect', ((results['intersect']/number_of_trials) * 100))
print('Percentage of non-intersect', ((results['non-intersect']/number_of_trials) * 100))
