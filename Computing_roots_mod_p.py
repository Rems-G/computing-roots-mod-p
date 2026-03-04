import numpy as np
import random


def modular_exponentiation(a,b,n):#Complexity
    x = a % b #1r
    res = 1 % b #1r
    m = n
    while m > 0: # *log2(n)
        if m & 1: # 1b 
            res = (res * x) % b # 1m + 1r
        m = m >> 1 # 1s
        x = (x*x)%b # 1m + 1r 
    return res #Total : log2(n)b ; 2log2(n)m ; (2log2(n)+2)r ; log2(n)s

def euler_criterion(a,p):# Complexity
    n= (p-1) >> 1 #1a + 1s
    legendre_a_p = modular_exponentiation(a,p,n) # log2((p-1)/2)b + 2log2((p-1)/2)m + (2log2((p-1)/2)+2)r + log2((p-1)/2)s
    if legendre_a_p == p-1 : # 1a
        legendre_a_p = legendre_a_p - p # 1a
    return legendre_a_p # Total : 3a ; (log2((p-1)/2)+1)s ; 2log2((p-1)/2)m ; log2((p-1)/2)b ; (2log2((p-1)/2)+2)r


#######
def Jacobi_2_n(n): #Complexity
    res = 0
    m = n%8 #1r
    if m == 1 or m == 7:
        res = 1
    elif m == 3 or m == 5:
        res = -1
    return res #Total : 1r



def Jacobi_symbol(a,p): #Complexity
    if a == 1 or p == 1:
        return 1
    b = a % p #1r
    res = 1
    if b == 0 :
        res = 0
    else :
        pow_two_divide_b = b & -b # 1b
        pow_2_b = pow_two_divide_b.bit_length() - 1 #.bit_length() is O(1). I consider it as a bitcheck : 1b + 1a
        if pow_2_b & 1: # 1b
            jacobi_2_i_p = Jacobi_2_n(p) # 1r
        else :
            jacobi_2_i_p = 1
        odd_b = b >> pow_2_b #1s
        parity = ((odd_b-1)*(p-1)) >> 2 #2a +1m +1s
        if parity & 1 : #1b
            prod_res = -1 
        else :
            prod_res = 1
        res = Jacobi_symbol(p,odd_b) * prod_res * jacobi_2_i_p #2m + ???
    return res


p = 10708729
values = [random.randint(1, p) for _ in range(100)]

for a in values:
    print(f"Number : {a}, Euler's criterion : {euler_criterion(a,p)}, Jacobi symbol : {Jacobi_symbol(a,p)}")

residues = []   
for i in range(1,101):
    residue = euler_criterion(i,p)
    print(f"Number : {i}, Euler's criterion : {residue}, Jacobi symbol : {Jacobi_symbol(i,p)}")
    if residue == 1 and i< 21 :
        residues.append(i)
print(residues)

def square_roots_compute(a,p):
    two_alpha = ((p-1) & -(p-1))
    alpha = two_alpha.bit_length()
    s = (p-1) >> alpha
    n = 1
    res = 1
    while res != -1:
        n += 1
        res  = Jacobi_symbol(n,p)
    b = modular_exponentiation(n,p,s)
    r_i = 0
    if modular_exponentiation(a,p,(p-1)>>2)  == -1 :
        r_i = 1
    else :
        r_i =0
    r = r_i
    i = 1
    while i < alpha-2 :
        a_i=(modular_exponentiation(b,p,-2*r)*a)%p
        if modular_exponentiation(a_i,p,pow(2,alpha-i-2)) == -1:
            r_i = 1
        else :
            r_i = 0
        print(r_i)
        r = r+ pow(2,i)*r_i
        i += 1
    print(r)
    return pow(n,r)

for i in residues:
    print(i)
    square_roots_compute(i,10708729)