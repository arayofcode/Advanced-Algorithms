"""
Given a string S, find the largest subsequence which is a palindrome
"""

# Helper function for brute forcing
def isPalindrome(S: str) -> bool:
    S = S.lower()
    for i in range(len(S) // 2 + 1):
        if S[i] != S[-1 -i]:
            return False
    return True

# Approach 1: Brute Force
from itertools import combinations

def bruteForce_PalinSubsequece(S: str) -> str:
    # Create subsequences and store them
    subsequences = set()
    for r in range(1, len(S) + 1):
        for c in combinations(S, r):
            subsequences.add(''.join(c))
    
    # Find largest palindromic subsequence
    maxPalindrome = S[0]
    for subsequence in subsequences:
        if isPalindrome(subsequence) and len(subsequence) > len(maxPalindrome):
            maxPalindrome = subsequence
    return maxPalindrome

# Dynamic Programming: Just finding length
def DP_PalinSubsequence_Length(S: str) -> int:
    if len(S) < 2:
        return len(S)
    if S[0] == S[-1]:
        return 2 + DP_PalinSubsequence_Length(S[1:-1])
    else:
        return max(DP_PalinSubsequence_Length(S[:-1]), DP_PalinSubsequence_Length(S[1:]))

# Dynamic Programming: Finding string
def DP_PalinSubsequence_String(S: str) -> str:
    if len(S) < 2:
        return S
    if S[0] == S[-1]:
        return S[0] + DP_PalinSubsequence_String(S[1:-1]) + S[-1]
    else:
        return max(DP_PalinSubsequence_String(S[:-1]), 
                   DP_PalinSubsequence_String(S[1:]), 
                   key=len)

"""
- Key is to understand overlapping subproblems. 
- S[1:] and S[:-1] will obv have overlaps
- Use hash table 
"""

# Memoized Length, bottom up
"""
For string of length 1, return 1

"""
def length_Memoized(S: str) -> int:
    memo = [[0 for _ in S] for _ in S]

    # Longest palindromic subsequence for length 1 is 1
    for i in range(len(memo)):
        memo[i][i] = 1

    for i in range(len(S)):
        for j in range(len(S)):