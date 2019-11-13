#Rotate through an array by a given number of cycles
#Example: if the array is [3, 4, 5, 6, 7], and the number of rotations is 3
#The output should be [6, 7, 3, 4, 5]

def solution(A,K):
    return A[K:] + A[:K]

#Known issue: if K > A.Length then no rotation takes place