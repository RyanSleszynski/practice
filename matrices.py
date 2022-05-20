
def is_matrix(matrix):
    """
    Returns a boolean value for whether a given list-of-lists is a matrix

    :param matrix: list of lists
    :return: Boolean
    """
    two_dimensional_check(matrix)
    index = 0
    # This goes through each item in the outer list
    while index < len(matrix):
        # if an element is found that is either not a list or not the same length as the first inner list
        # then it is not a matrix
        if type(matrix[index]) != list or len(matrix[0]) != len(matrix[index]):
            return False
        index += 1

    # if the function gets to this point that means it is a matrix
    return True


# number of iterations: len(M1) * len(M1[0])
def is_equal(M1, M2):
    """
    Returns whether two given matrices of the same size are identical

    :param M1: list-of-lists (n x m) size
    :param M2: list-of-lists (n x m) size
    :return:
    """
    # if one of the values passed is not a matrix this will raise a value error
    if is_matrix(M1) and is_matrix(M2):

        # if the length of the outer lists aren't the same they cannot be compared
        if same_size(M1, M2):

            # for each element in every row of both matrices check to see if they are equal.
            # If not equal return false, else continue checking
            for row in range(len(M1)):
                for col in range(len(M1[row])):
                    if M1[row][col] != M2[row][col]:
                        return False
            return True
        else:
            raise ValueError('is_matrix ValueError: These matrices rows are not of the same size.')
    else:
        raise ValueError('is_matrix ValueError: At least 1 of the values passed is not a matrix.')


# number of iterations: len(M1) * len(M1[0])
def add(M1, M2):
    """
    Returns a matrix that is the sum of two matrices

    :param M1: list-of-lists of size n x m
    :param M2: list-of-lists of size n x m
    :return: list-of-lists of size n x m
    """
    two_dimensional_check(M1)
    two_dimensional_check(M2)
    # if the matrices are of the same size they can be added
    if same_size(M1, M2):
        # because of mutability we must make a copy of only one of the passed matrices
        # because the resulting matrix will be of the same size as both passed matrices
        Msum = new_matrix(M1)

        # for every element in M1 we add the corresponding element from M2 and assign it to its proper place in Msum
        for row in range(len(M1)):
            for col in range(len(M1[row])):
                Msum[row][col] = M1[row][col] + M2[row][col]

        return Msum
    else:
        raise ValueError('add() ValueError: The passed matrices are not the same size')


# number of iterations: len(M1) * len(M1[0])
def subtract(M1, M2):
    """
    Returns a matrix that is the difference of two matrices

    :param M1: list-of-lists of size n x m
    :param M2: list-of-lists of size n x m
    :return: list-of-lists of size n x m
    """
    two_dimensional_check(M1)
    two_dimensional_check(M2)
    if same_size(M1, M2):
        Mdifference = new_matrix(M1)
        for row in range(len(M1)):
            for col in range(len(M1[row])):
                Mdifference[row][col] = M1[row][col] - M2[row][col]

        return Mdifference
    else:
        raise ValueError('subtract() ValueError: The passed matrices are not the same size')


# number of iterations in case one of the M1, and M2 is constant: len(non-constant_matrix) * len(non-constant_matrix[0])
# number of iterations in case both M1 and M2 are two-dimensional lists: len(M1) * len(M1[0]) * len(M2[0))
def multiply(M1, M2):
    # if one of the passed arguments is not a list then the user is trying to
    # multiply by a constant
    if isinstance(M1, (int, float)) and is_matrix(M2):
        result_matrix = create_matrix(M2)
        for row in range(0, len(result_matrix)):
            for col in range(0, len(result_matrix[row])):
                result_matrix[row][col] *= M1
        return result_matrix
    elif isinstance(M2, (int, float)) and is_matrix(M1):
        result_matrix = create_matrix(M1)
        for row in range(0, len(result_matrix)):
            for col in range(0, len(result_matrix[row])):
                result_matrix[row][col] *= M2
        return result_matrix

    # if both arguments passed are matrices and the columns of the first
    # equals the rows of the second then they can be multiplied
    elif is_matrix(M1) and is_matrix(M2) and len(M1[0]) == len(M2):
        result_matrix = [[0 for i in range(len(M2[0]))] for i in range(len(M1))]

        # for each row in M1...
        for m1_row in range(len(M1)):

            # ... and each column in M2...
            for m2_col in range(len(M2[0])):
                result = 0

                # ...we multiply the elements in the current row in M1
                # with elements from the current column of M2 and add them together
                for m1_col_and_m2_row in range(len(M2)):
                    result += M1[m1_row][m1_col_and_m2_row] * M2[m1_col_and_m2_row][m2_col]

                # once the all elements of a given column in M2 are multiplied then add the result to the result_matrix
                result_matrix[m1_row][m2_col] = result

        # print('Multiply number of iterations:', number_of_iterations)
        return result_matrix
    else:
        raise ValueError('multiply ValueError: These matrices cannot be multiplied.')


# number of iterations: num_rows * num_cols <please fill this else marks shall be deducted>
def transpose(M):
    if is_matrix(M):
        num_rows = len(M)
        num_cols = len(M[0])
        tp_matrix = [[None for _ in range(num_rows)] for _ in range(num_cols)]  # create new matrix with null values in each row and col
        for j in range(num_rows):
            for i in range(num_cols):
                tp_matrix[i][j] = M[j][i]  # new matrix rows equal original matrix columns
        return tp_matrix
    else:
        raise ValueError('transpose ValueError: the passed argument is not a two-dimensional matrix')


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


# number of iterations: len(row_with_most_columns) * len(M) <please fill this else marks shall be deducted>
def transposeLoL(M):
    two_dimensional_check(M)
    T = []
    max_col = 0
    # we find the maximum number of columns in the passed list of lists to be
    # used as a reference point of when to stop the loop
    for element in M:
        if len(element) > max_col:
            max_col = len(element)

    # for every column in M...
    for col in range(max_col):
        T.append([])

        # this variable solved the problem of when a column is not in row 'n' but is in row 'n+1'
        next_T_col = 0

        # ...and every row in M
        for row in range(len(M)):

            # if there is an element in the current row at the current column value
            # then add it to the transposed list (T)
            if len(M[row]) > col:
                T[col].append(0)
                T[col][next_T_col] = M[row][col]
                next_T_col += 1
    return T


def zero_matrix(M):
    if is_matrix(M):
        Z = new_matrix(M)

        for row in range(len(M)):
            for col in range(len(M[row])):
                if M[row][col] == 0:
                    for item in range(len(M[row])):
                        Z[row][item] = 0
                    for item in range(len(M)):
                        Z[item][col] = 0
        return Z
    else:
        raise ValueError('zero_matrix ValueError: the passed argument must be a two-dimensional matrix')


def same_size(matrix_1, matrix_2):
    # if the matrices have the same number of rows then we can check the columns
    if len(matrix_1) == len(matrix_2):
        row = 0
        # check the length of each row of both matrices to see if they are the same.
        # if they are not the same return False, else keep checking
        while row < len(matrix_1):
            if len(matrix_1[row]) != len(matrix_2[row]):
                return False
            row += 1

    # if the matrices do not have the same number of rows they are not the same size
    else:
        return False

    # if the function gets to this point that means the matrices are the same size
    return True



def create_matrix(end):
    position = 0
    matrix = []
    for row in range(end[0]+1):
        matrix.append([])
        for item in range(end[1]+1):
            matrix[row].append(position)
            position += 1
    return matrix


def new_matrix(matrix_1, matrix_2=None):
    if matrix_2 == []:
        changed_matrix = matrix_1[:]
        index = 0
        while index < len(matrix_1):
            changed_matrix[index] = matrix_1[index][:]
            index += 1
        return changed_matrix
    else:
        changed_matrix = [[0 for col in range(len(matrix_1[row]))] for row in range(len(matrix_1))]
        # for row in range(len(matrix_1)):
        #     changed_matrix.append([])
        #     for col in range(len(matrix_1[row])):
        #         changed_matrix[row].append(0)
        return changed_matrix


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


def two_dimensional_check(M):
    if not isinstance(M, list):
        raise TypeError('TypeError: the passed argument must be a list')
    for row in M:
        if not isinstance(row, list):
            raise TypeError('TypeError: at least one element of the passed argument is not a list')


# Find the number of unique possible paths from a given cell of a matrix to the end of the matrix
# For example, the number of possible paths from the cell 0 (coordinate (0,0)) to the cell 8 (coordinate (2,2))
# in the following maze is given as:
###################
# (0) # (1) # (2) #
###################
# (3) # (4) # (5) #
###################
# (6) # (7) # (8) #
###################
# The robot take only one step i.e. jumps only one cell at a time.
# The directions allowed to walk from a given cell are bottom, right, and diagonal (bottom-right),
# Remember you are NOT allowed to go back up, left, upper-left.
# In the above case, the unique paths are 13, as given below:
# ["01478",
# "0148",
# "01458",
# "0158",
# "01258",
# "03678",
# "0378",
# "03478",
# "0348",
# "03458",
# "0478",
# "048",
# "0458"]

####################
##### REQUIRED #####
####################


def count_paths(start, end):
    # here we are assigning the values from start to variables because
    # it is passed as a tuple thus it is editable
    start_row = start[0]
    start_col = start[1]

    # Base Case: if the "starting point" is the "ending point" then break
    # recursion and return a 1 indicating a single path
    if start_row == end[0] and start_col == end[1]:
        return 1

    # Recursive Case 1: if the robot is in the last row but not in the last column
    # then call the function again from a new starting point one column to the right of where
    # the robot is currently
    elif start_row == end[0] and start_col != end[1]:
        start_col += 1
        start = (start_row, start_col)
        return count_paths(start, end)

    # Recursive Case 2: If the robot is in the last column but not in the last row
    # then call the function again from a new starting point one row below where it is currently
    elif start_row != end[0] and start_col == end[1]:
        start_row += 1
        start = (start_row, start_col)
        return count_paths(start, end)

    # Recursive Case 3: If the robot is not in the last column and not in the last row then
    # check all possible routes from that point by going down one row first, then one column, then diagonal
    else:
        count = 0
        start_row += 1
        start = (start_row, start_col)
        count += count_paths(start, end)
        start_row -= 1
        start_col += 1
        start = (start_row, start_col)
        count += count_paths(start, end)
        start_row += 1
        start = (start_row, start_col)
        count += count_paths(start, end)
        return count

#
# def return_paths_helper(start_row, start_col, end_row, end_col, matrix):
#     list_of_paths = []
#     if start_row == end_row and start_col == end_col:
#         return str(matrix[end_row][end_col])
#     elif start_row == end_row and start_col != end_col:
#         return str(matrix[end_row][end_col]) + return_paths_helper(start_row, start_col+1, end_row, end_col, matrix)
#     elif start_row != end_row and start_col == end_col:
#         return str(matrix[end_row][end_col]) + return_paths_helper(start_row+1, start_col, end_row, end_col,matrix)
#     else:
#         list_of_paths.append(str(matrix[end_row][end_col]) + return_paths_helper(start_row + 1, start_col, end_row, end_col, matrix))
#         list_of_paths.append(str(matrix[end_row][end_col]) + return_paths_helper(start_row, start_col+1, end_row, end_col, matrix))
#         list_of_paths.append(str(matrix[end_row][end_col]) + return_paths_helper(start_row+1, start_col + 1, end_row, end_col, matrix))


def return_paths(start, end):
    # matrix = create_matrix((start[0], start[1]), (end[0], end[1]))
    # return return_paths_helper(start[0], start[1], end[0], end[1], matrix)
    # # here we are assigning the values from start to variables because
    # # it is passed as a tuple thus it is editable
    start_row = start[0]
    start_col = start[1]
    list_of_paths = []
    # Base Case: if the "starting point" is the "ending point" then break
    # recursion and return a 1 indicating a single path
    if start_row == end[0] and start_col == end[1]:
        return str((end[0] * (end[1] + 1)) + end[1])

    # Recursive Case 1: if the robot is in the last row but not in the last column
    # then call the function again from a new starting point one column to the right of where
    # the robot is currently
    elif start_row == end[0] and start_col != end[1]:
        start_col += 1
        start = (start_row, start_col)
        return str((start_row * (end[1] + 1)) + (start_col - 1)) + return_paths(start, end)

    # Recursive Case 2: If the robot is in the last column but not in the last row
    # then call the function again from a new starting point one row below where it is currently
    elif start_row != end[0] and start_col == end[1]:
        start_row += 1
        start = (start_row, start_col)
        return str((((start_row - 1) * (end[1] + 1)) + start_col)) + return_paths(start, end)

    # Recursive Case 3: If the robot is not in the last column and not in the last row then
    # check all possible routes from that point by going down one row first, then one column, then diagonal
    else:
        start_row += 1
        start = (start_row, start_col)
        # list_of_paths.append(str((start_row - 1) * (end[1] + 1) + start_col) + return_paths(start, end))
        list_of_paths.append(return_paths(start,end))
        start_row -= 1
        start_col += 1
        start = (start_row, start_col)
        # list_of_paths.append(str(start_row * (end[1] + 1) + (start_col - 1)) + return_paths(start, end))
        list_of_paths.append(return_paths(start, end))
        start_row += 1
        start = (start_row, start_col)

        # list_of_paths.append(str((start_row - 1) * (end[1] + 1) + (start_col - 1)) + return_paths(start, end))
        list_of_paths.append(return_paths(start, end))
        for item in list_of_paths:
            item = str((start_row - 1) * (end[1] + 1) + (start_col - 1)) + item

    # # Alternate Solution
    # # # here we are assigning the values from start to variables because
    # # # it is passed as a tuple thus it is editable
    # start_row = start[0]
    # start_col = start[1]
    # list_of_paths = []
    # # Base Case: if the "starting point" is the "ending point" then break
    # # recursion and return a 1 indicating a single path
    # if start_row == end[0] and start_col == end[1]:
    #     return str((end[0] * (end[1] + 1)) + end[1])
    #
    # # Recursive Case 1: if the robot is in the last row but not in the last column
    # # then call the function again from a new starting point one column to the right of where
    # # the robot is currently
    # elif start_row == end[0] and start_col != end[1]:
    #     start_col += 1
    #     start = (start_row, start_col)
    #     return str((start_row * (end[1] + 1)) + (start_col - 1)) + return_paths(start, end)
    #
    # # Recursive Case 2: If the robot is in the last column but not in the last row
    # # then call the function again from a new starting point one row below where it is currently
    # elif start_row != end[0] and start_col == end[1]:
    #     start_row += 1
    #     start = (start_row, start_col)
    #     return str((((start_row - 1) * (end[1] + 1)) + start_col)) + return_paths(start, end)
    #
    # # Recursive Case 3: If the robot is not in the last column and not in the last row then
    # # check all possible routes from that point by going down one row first, then one column, then diagonal
    # else:
    #     start_row += 1
    #     start = (start_row, start_col)
    #     # list_of_paths.append(str((start_row - 1) * (end[1] + 1) + start_col) + return_paths(start, end))
    #     list_of_paths.append(return_paths(start, end))
    #     start_col += 1
    #     start = (start_row, start_col)
    #     # list_of_paths.append(str(start_row * (end[1] + 1) + (start_col - 1)) + return_paths(start, end))
    #     list_of_paths.append(return_paths(start, end))
    #     start_row -= 1
    #     start = (start_row, start_col)
    #     # list_of_paths.append(str((start_row - 1) * (end[1] + 1) + (start_col - 1)) + return_paths(start, end))
    #     list_of_paths.append(return_paths(start, end))
    #     if start_row == 0 and start_col - 1 == 0:
    #         return str(' ' + list_of_paths[0] + ' ' + list_of_paths[1] + ' ' + list_of_paths[2]).replace(' ', ' ' + str(
    #             start_row * (end[1] + 1) + (start_col - 1)))
    #     else:
    #         return str(' ' + list_of_paths[0] + ' ' + list_of_paths[1] + ' ' + list_of_paths[2]).replace(' ', ' ' + str(
    #             start_row * (end[1] + 1) + (start_col - 1)))


####################
##### OPTIONAL #####
####################
# The following function is similar to count_paths but with the following change
# The robot will be able to take either 1 or 2 steps in the bottom, right, and diagonal (bottom-right) directions
def count_paths_12(start, end):
    # <feel free to write helper functions if you need to>
    pass

# The following function is similar to return_paths but with the following change
# The robot will be able to take either 1 or 2 steps in the bottom, right, and diagonal (bottom-right) directions


def return_paths_12(start, end):
    # <feel free to write helper functions if you need to>
    # This is same as count_paths_12 but with the expectation that you will either
    # print or return the list of all possible paths
    # just return the list_of_paths, the number of paths would be just len(list_of_paths)
    pass


if __name__ == "__main__":

    start = (0, 0)
    end = (2, 2)
    if count_paths(start, end) == 13:
        print('Passed for {} and {}'.format(start, end))
    else:
        print('Failed for {} and {}'.format(start, end))

    start = (1, 0)
    end = (2, 2)
    if count_paths(start, end) == 5:
        print('Passed for {} and {}'.format(start, end))
    else:
        print('Failed for {} and {}'.format(start, end))

    start = (1, 1)
    end = (2, 2)
    if count_paths(start, end) == 3:
        print(f'Passed for {start} and {end}')
    else:
        print(f'Failed for {start} and {end}')

    start = (0, 0)
    end = (3, 3)
    if count_paths(start, end) == 63:
        print(f'Passed for {start} and {end}')
    else:
        print(f'Failed for {start} and {end}')

    start = (0, 0)
    end = (2, 2)
    list_of_paths = []
    print(return_paths(start, end))
