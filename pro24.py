import sys, string, math
n1 = int(input())
k1 = 2**n1
L = []
for i in range(0,k1) :
    s1 = bin(i)[2:]
    j1 = len(s)
    if j < n1 :
        s = '0' * (n1-j) + s
    L.append(s)
for i in range(0,len(L)) :
    print(L[i])
