#!/usr/bin/python3
""" Minimum Operations
    """
def minOperations(n):
    if n <= 1:
        return 0  

    # To find the minimum operations to create n H characters, consider the following:
    # - If `n` can be factored into `a * b`, you can first create `a` characters,
    #   then copy and paste `b-1` times, leading to fewer operations.
    
    # Initialize operations count
    operations = 0
    factor = 2
    
    # Keep dividing `n` by its smallest factor (starting from 2 onwards)
    while factor * factor <= n:
        while (n % factor) == 0:
            # If `factor` is a divisor, then you can consider it for Copy All and Paste
            operations += factor  # One Copy All + `factor-1` pastes
            n //= factor  # Reduce `n` by this factor
        factor += 1  # Check next factor
    
    # If `n` is greater than 1, it's a prime factor itself
    if n > 1:
        operations += n  # The last remaining factor, indicating required operations
    
    return operations
