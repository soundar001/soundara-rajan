import sys, string, math

def factors1(n1) :
    L = []
    i = 2
    cnt = 0
    while n1 >1 :
        while n1%i == 0 :
            cnt += 1
            n1 //= i
        i += 1
    return cnt

n1 = int(input())
L = [input().split() for i in range(0,n1)]

for i in range(0,n1) :
    p = 1
    n1, k = L[i]
    n1, k = int(n1), int(k)

    for i in range(k+1,n1+1) :
        p = p*i
    a = factors1(p)
    print(a)
