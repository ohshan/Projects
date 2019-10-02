# Module 2: Encryption Module
# Input: The input here is the public information provided by the key setup
# module initiated by Bob in file public_key which contains the product of
# primes 'p' & 'q' which is n. Also holds the encrytion integer e.
# Output: The output here is the encrypted message that was in message.txt.
# The encrypted message is in the file 'ciphertext'.
# Description: Since Bob already did the key setup module, Alice now wants to
# send a message m to Bob such that m cannot be read by anybody who is
# eavesdropping on the medium of communication.
# Algorithms: Extended Euclidean algorithm for modular exponentiation.
# Execution: python3 module2.py
# Libraries:  - "Math" to add support for mathematical operations.
#             - "Random" to generate random numbers in the given bounds.
#             - "sys" to set my recursion limit to avoid infinite recursion.
import math
import random
import sys
sys.setrecursionlimit(1000000)

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

# Opening the file that contains the message that needs to be encypted and sent.
message = open("message.txt", "r")
m = message.read()
message.close()
# Make m an integer
m = int(m)

# Opens the file that contains all the public key information.
publicKey = open("public_key", "r")
nAndE = publicKey.read()
publicKey.close()
# Find n and e in the file.
n,e = nAndE.split()
# Turn n and e into integers.
n = int(n)
e = int(e)

# Encrypt the message m such that c = m^e (mod n) where c is ciphertext.
c = modExp(m, e, n)

# Create a file ciphertext and write the encrypted message to the file.
CT = open("ciphertext","w")
CT.write(str(c))
CT.close()
