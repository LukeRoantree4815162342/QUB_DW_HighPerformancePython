import numpy as np
big_number = 500
is_prime=lambda x: all(x % i != 0 for i in range(int(x))[2:])

def bad_np():
    global big_number
    primes = np.array([])
    for i in range(big_number):
        if is_prime(i):
            primes = np.append(primes,i)
    return primes

def normal_list():
    global big_number
    primes = []
    for i in range(big_number):
        if is_prime(i):
            primes.append(i)
    return primes

#bad_np()
normal_list()