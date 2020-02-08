def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
   
    n = 2
    while n <= x:
        if x % n == 0:
          return n
        n+=1
