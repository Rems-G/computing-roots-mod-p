import numpy as np
A = np.array([-1,-4,-3,1])
B = np.array([-1,-1,1])

A1 = np.array([-1,2,-1,1,-2,1])
B1 = np.array([-2,2,-1,1])

A2 = np.array([0,0,1])
B2 = np.array([1,1])


def deg(A):
    d = 0
    for i in range(len(A)):
        if A[i] != 0 :
            d = i
    return d


def divceucli(A,B):
    n = deg(A)
    m = deg(B)
    if n < m :
        return 0,A
    b = (A[n]/B[m])*B
    for i in range(n-m):
        b = np.insert(b,0,0)
    while A[len(A)-1] == 0:
        A = A[:-1]
    a = A - b
    Q = [A[n]/B[m]]
    n1 = deg(a)
    while n1 >= m :
        b = (a[n1]/B[m])*B
        for i in range(n1-m):
            b = np.insert(b,0,0)
        while a[len(a)-1] == 0:
           a = a[:-1]
        Q.append(a[n1]/B[m])
        a = a-b
        if deg(a) == 0:
            return np.array(Q[::-1]),a
        while a[len(a)-1] == 0:
            a = a[:-1]
        n1 = deg(a)
    return (np.array(Q[::-1]),a)


def PGCD(A,B):
    Rl = [B]
    Q,R = divceucli(A,B)
    Rl.append(R)
    print(Rl)
    while deg(R) > 0 :
        print(R)
        if deg(R) == 0 :
            return Rl[len(Rl)-1]
        print(Rl[len(Rl)-2])
        print(Rl[len(Rl)-1])
        Q,R = divceucli(Rl[len(Rl)-2],Rl[len(Rl)-1])
        Rl.append(R)
    if Rl[len(Rl)-1][deg(Rl[len(Rl)-1])] != 1 :
        Rl[len(Rl)-1] = Rl[len(Rl)-1]/Rl[len(Rl)-1][deg(Rl[len(Rl)-1])]
    return Rl[len(Rl)-1]


