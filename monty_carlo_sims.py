import random


def cords_intersect_in_circle(number_of_trials):
    """
    Runs a monty carlo simulation to find the probability of intersection of two cords
    through random selection of points on the circumference of a circle

    :param number_of_trials: the amount of trials the simulation should run
    :return: None
    """
    def first_point_generation(number_of_trials):
        a, b = 0, 360
        first_point_input = []
        for trial in range(number_of_trials):
            first_point = random.uniform(a, b)
            first_point_input.append(first_point)
        return first_point_input

    def second_point_generation(first_point_input: list, number_of_trials):
        a, b = 0, 360
        first_point_index = 0
        second_point_input = []
        for trial in range(number_of_trials):
            second_point = random.uniform(a, b)
            while first_point_input[first_point_index] == second_point:
                second_point = random.uniform(a, b)
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

    # del removes all previous input because it is zipped to a new object at this point
    del a_input, b_input, c_input, d_input
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

if __name__ == '__main__':
    cords_intersect_in_circle(100_000)