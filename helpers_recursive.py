from math import sqrt


def is_prime(whole_number, divisor=3):
    if not whole_number == int:
        raise TypeError("TypeError: is_prime function requires an int data type")

    if whole_number < 2 or whole_number % 2 == 0 and whole_number != 2 or whole_number% 5 == 0:
        return False
    elif whole_number == 2:
        return True
    else:
        if divisor % 5 == 0:
            divisor += 2
        if whole_number % divisor != 0 and divisor < sqrt(whole_number):
            return is_prime(whole_number, divisor + 2)
        if divisor >= sqrt(whole_number):
            return True
        else:
            return False


if __name__ == "__main__":
    print(is_prime(9))