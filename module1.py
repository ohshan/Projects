# Module 1: Key Setup Module
# Input: No input here. This module just sets up the public and private keys.
# Output: Uses the public and private keys and outputs them into their
# respective files, public_key & private_key.
# Description: If Bob wants to be able to receive messages from Alice without
# anybody else being able to read them if intercepted, then Bob should use
# the RSA encrytion scheme which begins here in the key setup module.
# Algorithms: Extended Euclidean algorithm for modular exponentiation and
# modular inverse. Recursive version of euclidean GCD. Fermat primality test.
# Execution: python3 module1.py
# Libraries:  - "Math" to add support for mathematical operations.
#             - "Random" to generate random numbers in the given bounds.
#             - "sys" to set my recursion limit to avoid infinite recursion.
import math
import random
import sys
sys.setrecursionlimit(1000000)

# Upper and lower bounds for the random number generator (100 digits to 200 digits)
lowBound = (10**100)+1
upBound = (10**200)-1

# Modular exponentiation function used across all modules.
# The parameters should be thought of in form: a^b (mod n).
def modExp(a, b, n):
    sol = 1 # Initializing the solution

    a = a % n # Update a if it is larger than the modulus

    while (b > 0):

        # If b is an odd integer take product of 'a' and 'sol'
        if ((b & 1) == 1):
            sol = (sol * a) % n

        # Bitwise operator making b even
        b = b >> 1
        a = (a*a) % n

    return sol

# Modular inverse function, a variation of extended euclidean algorith,
# used to find the decryption integer 'd'
def modInv(a, b):
    b0 = b
    x = 1
    y = 0

    if (b == 1):
        return 0

    while (a > 1):
        q = a // b # q is the quotient of a and b
        t = b # temp variable for b
        b = a % b # b is remainder
        a = t
        t = y
        y = x - q * y # update the values for x and y
        x = t

    # support for case where x is negative, makes x positive
    if (x < 0):
            x = x + b0

    return x

# Can be removed
# GCD algorithm used for debugging purposes
def GCD(x, y):
    if x == 0:
        return y

    return GCD(y%x, x)

# Function RPG stands for random prime generator. Generates a random number
# and checks for primality via the fermat primality test.
def RPG():
    # initialize z as the random integer between specified bounds
    z = random.randint(lowBound,upBound)

    # loops until z is odd because if z is an even number than it cannot be prime
    while ((z % 2) == 0):
        z = random.randint(lowBound,upBound)
        continue

    # Fermat primality test for rest of function.
    # If z is odd generate random int between 2 and z-1
    if ((z % 2) == 1):
        a = random.randint(2,z-1)
        x = modExp(a, z-1, z) # x = a^(z-1) (mod z)

    # if x = 1 then z is probabliy prime
    if (x == 1):
        return z

    # loops until we find a z that is probably prime, that is x = 1
    while (x != 1):
        z = random.randint(lowBound,upBound)
        a = random.randint(2,z-1)
        x = modExp(a, z-1, z)

    return z

# random primes 'p' & 'q' tested with fermat primality test
p = RPG()
q = RPG()
# 'n' is the product of primes, 'p' & 'q'
n = p*q
# phi is the phi function of 'n' (n = pq)
phi = (p-1)*(q-1)
# e was chosen via the project description with e = 2^16+1
e = (2**16)+1

# loop until the difference between p and q is greater than 10^95 and
# until the GCD of the encrytion integer e and phi(n) is congruent to 1.
while ((abs(p-q) < 10**95) and (GCD(e, phi) != 1)):
    p = RPG()
    q = RPG()
    n = p*q
    phi = (p-1)*(q-1)

# d is the decryption function in RSA found by d = e^(-1) (mod (p-1)*(q-1))
d = modInv(e, phi)

# creates a file for public key information (n and e)
publicKey = open("public_key", "w")
publicKey.write(str(n) + " ")
publicKey.write(str(e))
publicKey.close()
# creates a file for a private key information (p, q, d)
privateKey = open("private_key", "w")
privateKey.write(str(p) + " ")
privateKey.write(str(q) + " ")
privateKey.write(str(d))
privateKey.close()
