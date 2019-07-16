import sys, string, math
import sys
def minCoins(coins, m, V):
    if (V == 0):
        return 0
    res = sys.maxsize

    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V - coins[i])

            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
    return res
n,V = input().split()
n,V = int(n), int(V)
coins = [ int(x) for x in input().split()]
print( minCoins(coins, n, V))
