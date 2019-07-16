import sys, string, math
def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
     
        new_excl = excl if excl > incl else incl

        incl = excl + i
        excl = new_excl

    return (excl if excl > incl else incl)

n = int(input())
L = [ int(x) for x in input().split()]
print(find_max_sum(L))
