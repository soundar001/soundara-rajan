import sys, string, math
n1 = int(input())
k1 = 2**n1
L = []
for i in range(0,k1) :
    s1 = bin(i)[2:]
    j1 = len(s1)
    if j1 < n1 :
        s1 = '0' * (n1-j1) + s1
    L.append(s1)
for i in range(0,len(L)) :
    print(L[i])
