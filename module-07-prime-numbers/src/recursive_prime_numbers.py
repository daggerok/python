def is_prime(number):
    """
    Check if number is prime.
    :param number: Number to check.
    :return: "True" if number is prime, "False" otherwise.
    """

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def find_prime_number(start, end):
    """
    Recursive prime number search in range from start to end.
    :param start: Inclusive start.
    :param end: Inclusive end.
    :return: First prime number found in a range, "None" otherwise.
    """

    if start > end:
        return None

    if is_prime(start):
        return start

    return find_prime_number(start + 1, end)
