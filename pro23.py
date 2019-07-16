import sys,string
s1 = input()
x1 = 0
y1 = 0
dir = '+x1'

for c1 in s1 :
    if c1 == 'G' :
        if dir == '+x1' : x1 += 1
        elif dir == '-x1' : x1 -= 1
        elif dir == '+y1' : y1 += 1
        elif dir == '-y1' : y1 -= 1
        #print(x, y)
    elif c1 == 'R' :
        if dir == '+x1' : dir = '-y1'
        elif dir == '-x1' : dir = '+y1'
        elif dir == '+y1' : dir = '+x1'
        elif dir == '-y1' : dir = '-x1'
    elif c1 == 'L' :
        if dir == '+x1' : dir = '+y1'
        elif dir == '-x1' : dir = '-y1'
        elif dir == '+y1' : dir = '-x1'
        elif dir == '-y1' : dir = '+x1'

if x1==0 and y1==0 :
    print('yes')
else :
    print('no')
