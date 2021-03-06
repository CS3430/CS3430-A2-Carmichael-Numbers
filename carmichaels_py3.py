##################################################
## module: carmichaels_py3.py
## author: Misty Jenkins
## A#: A01489174
## finds Charmichael Numbers
## 09/15/2016
##################################################

from fermat_primes_py3 import is_fermat_prime
from math import sqrt

knownPrimes = set()

# returns true if n is a perfect square
def is_perfect_square(n):
    root = int(sqrt(n))
    if(root**2 == n):
        return True
    return False

# returns true if p divides n
def divides(p, n):
    return n%p == 0

# returns true if n is prime
def is_prime(n):
    if(n%2==0):
        return False
    if(n<2):
        return False

    global knownPrimes
    if(n in knownPrimes):
        return True
    else:
        for i in range(3, n//2, 2):
            if not (n%i):
                return False

    knownPrimes.add(n)
    return True

# returns true if n is a Carmichael number
def is_carmichael(n):
    if(n==1):
        return False
    if(is_prime(n)):
        return False

    divisors = set([1, n])
    # get divisors
    for i in range(3, n//2+1, 2):
        if(n%i == 0):
            divisors.add(i)

    for i in divisors:
        if(is_perfect_square(i) and i != 1):
            return False
        if(is_prime(i)):
            if(not divides(i-1, n-1)):
                return False

    return True

# returns a set object of Carmichaels in [x, y], where x and y are non-negative integers and x <= y
def find_carmichaels_in_range(x, y):
    return set([i for i in range(x, y) if is_carmichael(i)])

# returns a set of the first n Carmichael numbers beginning its search from 0
# as the numbers are added to that set they are printed out
def find_first_n_carmichaels(n):
    i = 0
    carmichaels = set()
    while len(carmichaels) < n:
        if(is_carmichael(i)):
            carmichaels.add(i)
            print(str(len(carmichaels)) + ") " + str(i))
        i += 1
    return carmichaels


# test code
numCarmichaels = 34
print("First " + str(numCarmichaels) + " Carmichael Numbers:")
carmichaelSet = find_first_n_carmichaels(numCarmichaels)
carmichaelSet = sorted(carmichaelSet)
print(str(carmichaelSet))

print("\n---Fermat Prime Tests---")
print('%10s' % "Carmichael" + \
      '%6s' % " Fermat" +\
      '%6s' % " Truth")
for c in carmichaelSet:
    print('%10s' % str(c) + "|" + \
          '%6s' % str(is_fermat_prime(c, 10)) + "|" + \
          '%6s' % str(is_prime(c)))

start = 100
end = 5000
print("\nCarmichael numbers between " + str(start) + " and " + str(end) + ":" )
print(str(find_carmichaels_in_range(start, end)))