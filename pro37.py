import sys,string
n = int(input())
L = [ int(x) for x in input().split()]
n = len(L)
if n==1 :
    print(1)
    sys.exit()
cnt = 0
for i in range(1,n-1) :
    if ((L[i] > L[i-1]) and (L[i] > L[i+1])) or ((L[i] < L[i-1]) and (L[i] < L[i+1])):
        cnt += 1
print(cnt)
