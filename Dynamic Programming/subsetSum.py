"""
Given an array A of size n and an integer s, find if sum of a subset equals s

Example: A = {10, 2, 4, 6, 9, 11}, s = 7
False

A = {10, 2, 4, 6, 9, 11}, s = 14
True, can use 10, 4
"""

def approach1(A, s, i=0):
    """
    For each element A_i in A, 
    It might be a part of sum, or it might not be. 
    Try using both possibilities
    """

    if s == 0:
        return True
    elif s < 0 or i >= len(A):
        return False
    else:
        return approach1(A, i + 1, s - A[i]) or approach1(A, i + 1, s)

A = [10, 2, 4, 6, 9, 11]
s = 300
result = approach1(A, s, 0)
print(result)