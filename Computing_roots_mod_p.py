import numpy as np
import random


def modular_exponentiation(a,b,n):
    x = a % b
    res = 1 % b
    m = n
    while m > 0:
        if m & 1:
            res = (res * x) % b
        m = m >> 1
        x = (x*x)%b
    return res

def euler_criterion(a,p):
    n= (p-1)//2
    legendre_a_p = modular_exponentiation(a,p,n)
    if legendre_a_p == p-1 :
        legendre_a_p = legendre_a_p - p
    return legendre_a_p


#######
def Jacobi_2_n(n):
    res = 0
    if n%8 == 1 or n%8 == 7:
        res = 1
    elif n%8 == 3 or n%8 == 5:
        res = -1
    return res



def Jacobi_symbol(a,p):
    if a == 1 or p == 1:
        return 1
    b = a % p
    res = 1
    if b == 0 :
        res = 0
    else :
        pow_two_divide_b = b & -b
        pow_2_b = pow_two_divide_b.bit_length() - 1
        if pow_2_b & 1:
            jacobi_2_i_p = Jacobi_2_n(p)
        else :
            jacobi_2_i_p = 1
        odd_b = b// pow_two_divide_b
        parity = ((odd_b-1)*(p-1))//4
        if parity & 1 :
            prod_res = -1
        else :
            prod_res = 1
        res = Jacobi_symbol(p,odd_b) * prod_res * jacobi_2_i_p
    return res


p = 10708729
values = [random.randint(1, p) for _ in range(100)]

for a in values:
    print(f"Number : {a}, Euler's criterion : {euler_criterion(a,p)}, Jacobi symbol : {Jacobi_symbol(a,p)}")
    
for i in range(1,101):
    print(f"Number : {i}, Euler's criterion : {euler_criterion(i,p)}, Jacobi symbol : {Jacobi_symbol(i,p)}")
