##################################################
## module: fermat_primes_py3.py
## author: Misty Jenkins
## A#: A01489174
## tests numbers using Fermat's Little Theorem
## 09/15/2016
##################################################

from random import randint

def is_even(e):
    return not bool(e % 2)

def remainder(a, b):
    return a % b

def expmod(b, e, m):
    if (e == 0):
        return 1
    elif (is_even(e)):
        x = expmod(b, e / 2, m);
        return remainder(x * x, m)
    else:
        return remainder(b * expmod(b, e - 1, m), m)

def fermat_test(n):
    if (n < 2):
        return False
    elif (n == 2):
        return True

    a = randint(2, n - 1)
    return expmod(a, n, n) == a


def is_fermat_prime(n, num_times):
    if (num_times == 0):
        return True;
    elif (fermat_test(n)):
        return is_fermat_prime(n, num_times - 1);
    else:
        return False;
