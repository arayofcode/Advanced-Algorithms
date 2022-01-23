"""
You have a rod of size n and a table that tells you what's the price at
which you can sell rod of size i. Cut the rod such that you can have
maximum revenue. 

Given: n, Prices

Optimized Solution Equation

Optimized(n) = Optimized(n - i) + Price[i]
S(n) = S(n - i) + O(1)

Time complexity = O(n^2) after memoization
"""
n = 5
Prices = [0, 5, 7, 11, 14, 19]
# For memoization
REVENUE = [0] + [-1] * n
# Stores the i from Optimized Solution equation, S[n] is Prices[i]
S = [0] * (n + 1)


def rodCutting(n, Price):
    # Memoization thing, reduces time complexity
    if REVENUE[n] >= 0:
        return REVENUE[n]

    # For calculating maximum revenue
    maxPrice = -1
    for i in range(1, n + 1):
        tmp = Price[i] + rodCutting(n - i, Price)
        if tmp > maxPrice:
            S[n] = i
            maxPrice = tmp
    # Storing revenue generated with Price[i] here
    REVENUE[n] = maxPrice
    return maxPrice
    
rodCutting(n, Prices)
print(REVENUE[n])

# Calculation of the pieces that give maximum answer
answer = []
j = n
while j > 0:
    answer.append(S[j])
    j -= S[j]

# Prints the pieces
print(answer)