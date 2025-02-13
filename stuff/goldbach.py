# Goldbach's Conjecture Check
#
# This script contains functions to check if an even number greater than 2
# can be expressed as the sum of two prime numbers, in line with Goldbach's 
# conjecture. The conjecture states that every even integer greater than 2 
# can be written as the sum of two primes.
#
# Functions:
# - is_prime(n): Returns True if n is a prime number, otherwise False.
# - goldbach_check(even_num): Given an even number greater than 2, returns
#   a pair of prime numbers that add up to the even number, or an error message
#   if the number is invalid.
#
# Example Usage:
# - goldbach_check(4) should return (2, 2)
# - goldbach_check(6) should return (3, 3)
# - goldbach_check(8) should return (3, 5)


# stole this one off of wikipedia
# "in mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit"
# basically a way to find all prime numbers to a point which you decide
# i might be explaining this wrong because i don't really understand ts

# code below uses a application of the sieve to generate prime numbers for use to check against the goldbach's conjecture thing
def sieve_of_eratosthenes(limit):
    """ 
    Returns a list of primes up to the limit using the Sieve of Eratosthenes 
    for efficient prime number generation.
    """
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]

def is_prime(n):
    """
    Checks if a given number n is a prime number.

    Args:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, otherwise False.

    for noobs like me, bool = boolean, specifically the "Boolean data type" by George Boole
    george boole so cool
    wait did that rhyme
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_check(even_num):
    """
    Checks if a given even number greater than 2 can be expressed as the sum of two primes.

    According to Goldbach's conjecture, every even number greater than 2 should
    be the sum of two prime numbers. This function finds such a pair if possible.

    Args:
    even_num (int): The even number to check.

    Returns:
    tuple: A tuple of two prime numbers that sum up to even_num, or a string
           message if the number is not valid (e.g., not even or <= 2).
    """
    if even_num <= 2 or even_num % 2 != 0:
        return "Not an even number greater than 2!"
    
    # Generate primes up to the given number using the Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(even_num)
    
    # Try finding two primes that sum up to the even number
    for p1 in primes:
        p2 = even_num - p1
        if p2 in primes:
            return p1, p2  # Found the pair of primes
    
    return "No pair found"  # In case no pair is found (should not happen for valid input)

# Testing the function with some even numbers (should work)
print(goldbach_check(4))  # Should return (2, 2)
print(goldbach_check(6))  # Should return (3, 3)
print(goldbach_check(8))  # Should return (3, 5)
# feel free to test with your own numbers
