def fibonacci_double_digits(n):
    """
        Find the index of the first term in the Fibonacci sequence with n digits.

        The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
        starting with 1 and 1. This function calculates terms of the Fibonacci sequence
        until it finds the first term that has the desired number of digits.

        Parameters:
        n (int): The number of digits of the Fibonacci term to find.

        Returns:
        int: The index of the first Fibonacci term that has 'n' digits.
    """

    # This is F_0
    f_old = 1
    # This is F_1
    f_new = 1
    # Hence, the new index starts at 2
    index = 2

    # Calculate the sequence
    while True:
        # Check length by casting to string
        if len(str(f_new)) == n:
            # Return number and index;
            # Technically the question only asks for the latter, but I'm including it here so you can check
            return f_new, index
        # Calculate the next element in the sequence
        temp = f_old + f_new
        f_old = f_new
        f_new = temp
        # Increase index
        index += 1


# Calling the function with 8 returns the number 14,930,352 at Fibonacci index 36
print(fibonacci_double_digits(8))
