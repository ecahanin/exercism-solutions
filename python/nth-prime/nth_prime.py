def prime(number):
    if number < 1:
        raise ValueError('not a meaningful input')
    primes = [2]
    n = 3
    while len(primes) < number:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes[-1]
    

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

