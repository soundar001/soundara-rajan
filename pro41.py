import sys,string
n0,n1 = input().split()
n0,n1 = int(n0),int(n1)
if n1 > (2+2*n0) :
    print(-1)
    sys.exit()
if n0 > n1-1 :
    print(-1)
    sys.exit()
s = ''
if n1-n0 == 1 :
    s = '1'+'01'*n0
    print(s)
    sys.exit()
while n1 > n0 and n0 > 0:
    if n1-n0 == 1 :
        break
    n1 -= 2
    n0 -= 1
    #print(n1,n0)
    s += '110'
if n1-n0 == 1 :
    s += '10'*n0+'1'
    print(s)
    sys.exit()
if n1 > 2 and n0==0 :
    print(-1)
    sys.exit()
elif n0==1 and n1==1 :
    s += '0'+'1'*n1
elif n0==1 and n1==2 :
    s += '101'
elif n0==0:
    s += '1'*n1
print(s)
