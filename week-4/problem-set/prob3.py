def F(n, memo):
    if n < 3:
        return 1
    else:
        if memo[n] == -1:
            memo[n] = F(n-1, memo) + F(n-2, memo)
        return memo[n]

n = 10
memo = [-1] * (n + 1)
result = F(n, memo)

print(f"The result of F({n}) is: {result}")