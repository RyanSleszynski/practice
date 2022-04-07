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


def reverse_recursive(L, index=0):
    if index >= len(L) // 2:
        return L
    else:
        L[index] = L[index] ^ L[(index * -1) - 1]
        L[(index * -1) - 1] = L[index] ^ L[(index * -1) - 1]
        L[index] = L[index] ^ L[(index * -1) - 1]
        return reverse_recursive(L, index + 1)


def palindrome_recursive(text):
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and palindrome_recursive(text[1:-1])


if __name__ == "__main__":
    if not is_prime(0):
        print("Passed is_prime recursive")
    else:
        print("Failed is_prime recursive")

    text = 'racecar '
    print(palindrome_recursive(text))