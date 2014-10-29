def isprime(n):
    if n < 2:
        return False
    elif n == 2: 
        return True
    for x in range(2,n-1):
        if not n % x: return False
    return True

def primesLessThanEqualTo(n):
    primes = []
    x=2
    for x in range(2,n):
        if isprime(x):
            primes.append(x)
    return primes
    
print str(primesLessThanEqualTo(20))
