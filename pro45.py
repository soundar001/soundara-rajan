import sys, string, math

s = input()
if s == s[::-1] :
    print('yes')
    sys.exit()
k = 0
for c in s[::-1] :
    if c == '0' :
        k += 1
    else :
        break
s2 = '0'*k + s

if s2 == s2[::-1] :
    print('yes')
else :
    print('no')
