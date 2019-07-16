import sys, string, math

n1 = int(input())
L1 = [ int(x) for x in input().split()]
L1.sort()

cnt = 0
for i in range(0,n1) :
    #print(i+1, L1[i], sum(L1[:i]),L1[i]-sum(L1[:i]))
    if L1[i]-sum(L1[:i]) >= 0 :
        cnt += 1

print(cnt)
