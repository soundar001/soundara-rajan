import sys, string, math


def isPrime(n) :
    if n <= 1 : return False
    if n==2 or n==3 : return True
    a = int(math.sqrt(n)+1)
    for i in range(2,a+1) :
        if n%i == 0 :
            return False
    return True

def factors1(n) :
    L = []
    i = 2
    while n >1 :
        while n%i == 0 :
            L.append(i)
            n //= i
        i += 1
    return L
n,k = input().split()
n,k = int(n), int(k)
if k==0 :
    print(n)
    sys.exit()
a = 10**k
if isPrime(n) :
    print(n * a)
    sys.exit()
s = str(n)[::-1]
cnt0 = 0
for c in s :
    if c=='0' :
        cnt0 += 1
    else :
        break
if cnt0 >= k :
    print(n)
    sys.exit()
L = factors1(n)

cnt2 = L.count(2)
cnt5 = L.count(5)
if cnt2 + cnt5 == 0 :
    print(n * a)
    sys.exit()

if cnt2 < k and cnt5 < k :
    while 2 in L : L.remove(2)
    while 5 in L : L.remove(5)
elif cnt2 < cnt5 :
    while 2 in L :
        L.remove(2)
    if cnt5 > k :
        for i in range(k) :
            L.remove(5)
elif cnt5 < cnt2 :
    while 5 in L :
        L.remove(5)
    if cnt2 > k :
        for i in range(k) :
            L.remove(2)
p = 1
for x in L :
    p = p * x
a = p * 10**k
print(a)
