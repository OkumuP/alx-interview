#!/usr/bin/python3
"""Prime Game module"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of ints where each int n is
        a set of consecutive int starts from 1 up to and including n.

    Returns:
        string: The name of the player who wins the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # Initialize scores
    ben = 0
    maria = 0
    # Create a list 'a' of length sorted(nums)[-1] + 1 with elements init to 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # Set the first two elements of the list to 0, a[0] and a[1], are set to 0
    # because 0 and 1 are not prime numbers
    a[0], a[1] = 0, 0
    # Generate array of prime numbers
    for i in range(2, len(a)):
        rm_multiples(a, i)
    # Play each round of the game
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determines the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        ls (list of int): An array of possible prime numbers.
        x (int): The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
