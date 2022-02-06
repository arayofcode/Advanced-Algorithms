"""
Given grid of size m*n, you begin from top left and need to reach bottom right
Find number of possible ways to do this. 
Constraint: You can move only down or right

Example:
findPaths(1, 1) -> 1
findPaths(1, 3) -> 3
"""

def findPaths_firstApproach(rows, columns):
    """
    Once you move down, you cannot move up, essentially decreasing size to 
    (rows - 1) * columns
    Similarly, once you move right, you cannot go left so size becomes
    rows * (columns - 1)
    For row = 1 or column = 1, there is only one way, either all down or left

    Time complexity: O(2^{m+n}) and Space = O(m + n)
    """

    if rows < 1 or columns < 1:
        return 0
    if rows == 1 or columns == 1:
        return 1

    # Just add all paths found by going down or right and return them
    return findPaths_firstApproach(rows - 1, columns) + findPaths_firstApproach(rows, columns - 1)

"""
findPaths_firstApproach() can have overlaps 
given from both ways you might reach similar subgrid.
-> Need to memoize
"""

def findPaths_Memoized(rows: int, columns: int, memo : dict = {}) -> int:
    """
    Use the previous code, but memoize the subgrids
    Have a dict and use rows and columns as keys. 
    If key present in memo, return it else calculate the value

    Time Complexity = O(m*n) and Space = O(m + n)
    """
    
    key : str = str(rows) + "," + str(columns)

    if key in memo.keys():
        return memo[key]

    if rows < 1 or columns < 1:
        return 0
    if rows == 1 or columns == 1:
        return 1
    
    memo[key] = findPaths_Memoized(rows - 1, columns, memo) + findPaths_Memoized(rows, columns - 1, memo)
    return memo[key]

# result = findPaths_firstApproach(3, 1)
result = findPaths_Memoized(42, 42)
print(result)