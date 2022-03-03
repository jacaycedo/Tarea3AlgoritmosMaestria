import sys
import math

def esPrimo(numero):
    for i in range(3, math.floor(math.sqrt(numero)), 2):
        if numero % i == 0: return False
    return True

def gcd2(a , b):
    if b == 0:
        answer = {a,1,0}
        return answer
    answerp = gcd2(b, a%b)
    q = math.floor(a/b)
    answer = {answerp[0], answerp[2], answerp[1]-q*answerp[2]}
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
    n = p*q
    m = (p-1)*(q-1)
    e = 3
    while gcd2(m,e)[0] != 1 :
        e +=2
    
    return 1

#Argv
# 0: File Name
# 1: Min range for prime generation
# 2: Max range for prime generation
if __name__== "__main__" :
    arguments = sys.argv
    print("Verifying the data ")
    print("The lower range to generate the prime numbers is {} and the maximum range is {}".format(arguments[1], arguments[2]))
