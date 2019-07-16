import sys, string, math

n = int(input())
L = [0] + [ int(x) for x in input().split()]
Lsum = [0 for i in range(0,n+4)]
np = 2
A = 0
B = 1
Lmax = []
for i in range(0,n+1) :
    Lmax.append([0,0])

for i in range(n,0,-1) :
    Lsum[i] = L[i] + Lsum[i+1]
    if i == n :
        Lmax[i][A] = Lmax[i][B] = L[i]
    else :
        Lmax[i][A] = max(Lmax[i + 1][A], L[i] + Lsum[i + 1] - Lmax[i + 1][B])
        Lmax[i][B] = max(Lmax[i + 1][B], L[i] + Lsum[i + 1] - Lmax[i + 1][B])
Amax = Lsum[1] - Lmax[1][B]
print(Amax, Lmax[1][B])
