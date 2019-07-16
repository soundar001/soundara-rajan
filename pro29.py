import sys, string, math
import sys,string
def dgtSum(n1) :
    sum1 = 0
    while n1 :
        sum1 += n1%10
        n1 //= 10
    return sum1
n1 = int(input())
L = []
cnt = 0
if n1 <= 5000 :
    for i in range(1,n1) :
        if i + dgtSum(i) == n1 :
            cnt += 1
            L.append(i)
    print(cnt)
    print(*L)
else :
    for i in range(n1-1000,n1) :
        if i + dgtSum(i) == n1 :
            cnt += 1
            L.append(i)
    print(cnt)
    print(*L)
