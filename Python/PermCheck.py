"""
Check if a list is a permutation
"""

def permCheck(A):
    print(A.sort())
    for i in range(0, len(A)):
        if i < (len(A)-1):
            if abs(A[i] - A[i+1]) != 1:
                return 0
            else:
                continue
        if i == (len(A)-1):
            return 1