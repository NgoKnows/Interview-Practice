def ways_to_skip(n, memo=None):
    if memo is None:
        memo = {}

    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1

    if n not in memo:
        memo[n] = ways_to_skip(n-1, memo) + ways_to_skip(n - 2, memo) + ways_to_skip(n - 3, memo)
    return memo[n]

print(ways_to_skip(3))
