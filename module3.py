# Module 3: Decryption Module
# Input: The input here is the ciphertext, private key and public key.
# Output: The output here is the decrypted message that was in ciphertext.
# The decrypted message is in the file decrypted_message.
# Description: Now that Alice has sent her ciphertext Bob can decrypt it and
# see the original message.
# Algorithms: Extended Euclidean algorithm for modular exponentiation.
# Execution: python3 module3.py
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

# Open the file with the public key information and extract it.
publicKey = open("public_key", "r")
nAndE = publicKey.read()
publicKey.close()
# Find n and e in the file.
n,e = nAndE.split()
# Turn n and e into integers.
n = int(n)
e = int(e)

# Open the file with the private key information and extract it.
privateKey = open("private_key", "r")
pqAndD = privateKey.read()
privateKey.close()
# Find p, q, and d in the file.
p,q,d = pqAndD.split()
# Make p, q, and d integers.
p = int(p)
q = int(q)
d = int(d)

# Open the ciphertext file and extract it into a variable c.
CT = open("ciphertext", "r")
c = CT.read()
CT.close()
# Make c an integer.
c = int(c)

# Compute the decrypted message m = c^d (mod n)
m = modExp(c, d, n)

# Create a file that contains the decrypted message.
DM = open("decrypted_message", "w")
DM.write(str(m))
DM.close()
