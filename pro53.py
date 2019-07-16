import sys, string, math
s = input()
s = s.lower()
s2 = string.ascii_lowercase

for c in s2 :
    if c not in s :
        print('no')
        sys.exit()
print('yes')
