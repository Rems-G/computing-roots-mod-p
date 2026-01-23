import numpy as np
import random
print( bin(1))
def euler_criterion(a,p):
    n= (p-1)//2
    x = a % p
    legendre_a_p = 1 % p
    bin_n = bin(n)[2:]
    while len(bin_n) > 0:
        if bin_n[-1] == "1":
            legendre_a_p = (legendre_a_p * x) % p
        x = (x*x)%p
        bin_n = bin_n[:-1]
    if legendre_a_p == p-1 :
        legendre_a_p = legendre_a_p - p
    return legendre_a_p

p = 5
values = [random.randint(1, p) for _ in range(100)]

tens = np.arange(1,101)

for a in values:
    print(a, euler_criterion(a,p))
    
for i in range(1,101):
    print(i, euler_criterion(i,p))

