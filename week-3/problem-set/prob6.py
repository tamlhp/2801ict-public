import numpy as np

def count_dynamic_programming(coins, n, sum):
    table = np.zeros((n, sum+1), dtype=int)
    table[:, 0] = 1

    for i in range(n):
        for j in range(1, sum+1):
            if coins[i] > j:
                table[i][j] = table[i-1][j]
            else:
                ways_exclude = table[i-1][j]
                ways_include = table[i][j-coins[i]]
                table[i][j] = ways_exclude + ways_include
    return table[-1][-1]

print(count_dynamic_programming([1,2,3], 3, 4))