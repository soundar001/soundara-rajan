import sys, string, math
s1 = input()
s2 = input()
s3 = string.ascii_lowercase
L = []

for i in range(0, len(s1)) :
    k = ord(s1[i]) + s3.index(s2[i]) + 1
    if k > ord('a')+25 :
        k -= 26
    
    L.append(chr(k))
s4 = ''.join(L)
print(s4)
