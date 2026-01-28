import numpy as np
import random


def modular_exponentiation(a,b,n):
    #I'll keep using bin() for now until I can think of something better, at least it works, even if it's not the fastest method
    x = a % b
    res = 1 % b
    bin_n = bin(n)[2:]
    while len(bin_n) > 0:
        if bin_n[-1] == "1":
            res = (res * x) % b
        bin_n = bin_n[:-1]
        x = (x*x)%b
    return res

def euler_criterion(a,p):
    n= (p-1)//2
    legendre_a_p = modular_exponentiation(a,p,n)
    if legendre_a_p == p-1 :
        legendre_a_p = legendre_a_p - p
    return legendre_a_p

p = 10708729
values = [random.randint(1, p) for _ in range(100)]

for a in values:
    print(a, euler_criterion(a,p))
    
for i in range(1,101):
   print(i, euler_criterion(i,p))

