import math

# Note: This is a brute force / naive solution and not particularly elegant;


def evenly_divisible(n):
    """
        Finds the smallest positive number that is evenly divisible by all numbers from 1 to n.

        Parameters:
        n (int): The upper bound of the range (inclusive) to check for even divisibility.

        Returns:
        int: The smallest positive number that is evenly divisible by all numbers from 1 to n.
    """

    # The factorial is the naive upper limit, but we're looking for numbers smaller than that
    upper = math.factorial(n)
    numbers = []

    # So lets check all numbers smaller than the factorial of n
    for number in range(1, upper+1):
        # Set flag to True
        flag = True
        # Check *all* numbers to n and if it doesn't work for one of them, stop, set flag to false and move on with life
        for j in range(1, n+1):
            if (number % j) != 0:
                flag = False
                break;

        # Technically not necessary to collect *all*, since the first one we find will be the smallest
        if flag:
            numbers.append(number)
    return min(numbers)


# The answer is 2520; As said, this solution is very inefficient (e.g., try 12 to see that)
print(evenly_divisible(12))