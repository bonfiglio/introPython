def fizzbuzz(n):
    """Return the factorial of n, an exact integer >= 0.
    >>> [fizzbuzz(n) for n in range(1,10)]
    [1, 2, 'fizz ', 4, 'buzz', 'fizz ', 7, 8, 'fizz ']
    >>> fizzbuzz(30)
    'fizz buzz'
    """
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")

    risp = ''
    if n % 3 == 0:
        risp = 'fizz '
    if n % 5 == 0:
        risp += 'buzz'
    if risp != '':
        return risp
    else:
        return n


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
