from math import sqrt


def is_prime(whole_number, divisor=3):
    # After testing 10,000 inputs 10,000 times each this function is about 0.0018 sec slower on average
    # compared to its iterative form
    if not type(whole_number) == int:
        raise TypeError("TypeError: is_prime function requires an int or float data type")

    if whole_number < 2 or whole_number % 2 == 0 and whole_number != 2 or whole_number % 5 == 0:
        return False
    elif whole_number == 2:
        return True
    else:
        if divisor % 5 == 0:
            divisor += 2

        if whole_number % divisor != 0 and divisor < sqrt(whole_number):
            return is_prime(whole_number, divisor + 2)
        elif divisor > sqrt(whole_number):
            return True
        else:
            return False


if __name__ == "__main__":
    if not is_prime(981433213):
        print("Passed is_prime recursive")
    else:
        print("Failed is_prime recursive")