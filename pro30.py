    
import sys, string, math
n = int(input())
if n==10 :
    print('yes')
    sys.exit()
s = str(n)
if len(s) <= 3 :
    if n%8 == 0 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
s2 = s[-3:]
n2 = int(s2)
if n2 == 0 :
    print('yes')
    sys.exit()
if n2%8 == 0 :
    print('yes')
    sys.exit()
s2 = s[:-1]
n2 = int(s2)
#print(s2,n2)
if n2%8 == 0 :
    print('yes')
    sys.exit()
s2 = s[:-2] + s[-1]
n2 = int(s2)
#print(s2,n2)
if n2%8 == 0 :
    print('yes')
    sys.exit()
s2 = s[:-3] + s[-2:]
n2 = int(s2)
#print(s2,n2)
if n2%8 == 0 :
    print('yes')
    sys.exit()
print('no')
