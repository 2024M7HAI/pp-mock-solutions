# This solution is the explicit one and verbose:
def power_dictionary_explicit(n):
    """
    Parameters:
    n (int): The ending number of the range (inclusive).

    Returns:
    dict: A dictionary where each key is a number in the range from 1 to n and its value is the square of the key.
    """
    squares_dict = {}
    for i in range(1, n+1):
        squares_dict[i] = i ** 2

    return squares_dict


# This solution is more 'Pythonic'
def power_dictionary_pythonic(n):
    """
    Parameters:
    n (int): The ending number of the range (inclusive).

    Returns:
    dict: A dictionary where each key is a number in the range from 1 to n and its value is the square of the key.
    """
    return {i: i ** 2 for i in range(1, n+1)}

print(power_dictionary_explicit(10))
print(power_dictionary_pythonic(10))