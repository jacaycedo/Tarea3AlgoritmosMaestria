import sys
import math
import time
from random import randint

def esPrimo(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd2(a , b):
    if b == 0:
        answer = [a,1,0]
        return answer
    answerp = gcd2(b, a%b)
    q = math.floor(a/b)
    answer = [answerp[0], answerp[2], answerp[1]-q*answerp[2]]
    return answer

def solveModularEquation(a,b,n):
    extgcd = gcd2(a,n)
    d = extgcd[0]
    x1 = extgcd[1]
    if b % d > 0 :
        return []
    q = math.floor(b/d)
    q2 = math.floor(n/d)
    answer = [None] * d
    answer[0] = (x1 * q) % n
    i = 1
    for i in range(d):
        answer[i] = (answer[0] + i * q2) % n
    return answer

def rsa (p , q):
    print("For the values of p and q we have the following internal values for rsa:")
    n = p*q
    m = (p-1)*(q-1)
    e = 3
    while gcd2(e,m)[0] != 1 :
        e +=2
    d = solveModularEquation(e,1,m)[0]
    print("\t n = {} \n\t m = {} \n\t e = {} \n\t d = {}".format(n,m,e,d))
    print("The public key is the tuple: \n\t<e,n> = <{},{}> \n\tDefined by:  \n\t\t P(x; e,n) = x^e mod n \n\t\t P(x; {},{}) = x^{} mod {}".format(e,n, e,n,e,n))
    print("The private key is the tuple: \n\t<d,n> = <{},{}> \n\tDefined by:  \n\t\t S(y; d,n) = y^d mod n \n\t\t P(y; {},{}) = y^{} mod {}".format(d,n, d,n,d,n))
    
# Argumests list
# 0: File Name
# 1: Min range for prime generation
# 2: Max range for prime generation
if __name__== "__main__" :
    arguments = sys.argv
    lowerRange, higherRange = int(arguments[1]), int(arguments[2])
    ini = time.time()
    print("Verifying the data ")
    print("Range  \n\tMinimun Range: {} \n\tMaximum range is {} \n".format(lowerRange, higherRange))
    prime1 = randint(lowerRange, higherRange)
    while not esPrimo(prime1):
        prime1 = randint(lowerRange, higherRange)
    
    prime2 = randint(lowerRange, higherRange)
    while not esPrimo(prime2) or prime1==prime2 :
        prime2 = randint(lowerRange, higherRange)
    print("The generated numbers are: \n\t p = {}\n\t q = {} \n".format(prime1, prime2))
    print("Calculating RSA ...")
    rsa(prime1, prime2)
    fin = time.time()
    print("It lasted {} s to complete the process".format((fin-ini)))


