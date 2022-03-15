import random
import time
import helpers

# Setup trials
max_value = 100
number_of_trials = 1000  # you can change this number to make the testing faster.
number_of_trials_per_input = 1000
# Setting the seed to make sure that the same random list is generated every time with the same parameters
random.seed(123)  # If you comment this line, you will get different list every time for the same parameters

input_list = [[int(random.random() * max_value) for i in range(number_of_trials)] for i in range(number_of_trials)]
for input_list_item in input_list:
    helpers.sort(input_list_item, "asc")
input_list_order = [random.choice(["asc", "desc"]) for i in range(number_of_trials)]
print("sort trials:")
# Time taken in mean_recursive
total_time_taken = 0
for item_list, item_order in zip(input_list, input_list_order):  # run for all the input
    total_time_taken_current_trial = 0
    for trial in range(number_of_trials_per_input):  # now run multiple times for every input
        start_time = time.time()
        helpers.is_sorted(item_list, item_order)
        end_time = time.time()
        time_taken_current_trial = end_time - start_time
        total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
    total_time_taken = total_time_taken + total_time_taken_current_trial

print('average time taken by is_sorted using for:', (total_time_taken) / number_of_trials)

# Time taken in mean_iterative
# we will use the same setup and input list as recursion so the comparison is fair
total_time_taken = 0
for item_list, item_order in zip(input_list, input_list_order):  # run for all the input
    total_time_taken_current_trial = 0
    for trial in range(number_of_trials_per_input):  # now run multiple times for every input
        start_time = time.time()
        helpers.is_sorted_while(item_list, item_order)
        end_time = time.time()
        time_taken_current_trial = end_time - start_time
        total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
    total_time_taken = total_time_taken + total_time_taken_current_trial

print('average time taken by is_sorted using while:', (total_time_taken) / number_of_trials)