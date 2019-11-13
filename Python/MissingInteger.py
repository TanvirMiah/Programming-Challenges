"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def missingInteger(A):
    #Sort array so the negative numbers (if any) are at the front
    A.sort()
    #Remove negative numbers from the array
    A = [number for number in A if number >=0]
    #If after removing negative numbers there arer no numbers left, return 1
    if len(A) == 0:
        return 1
    else:
        #Set j to the value of the first array 
        j = A[0]
        for i in range(0, len(A)):
            #print("J is equal to", j)
            if j > 0:
                if i < (len(A) - 1):
                    #f they equal each other AND the first value is 1
                    if A[i] == j and A[0] == 1:
                        #print("j is equal to", j)
                        j += 1
                    #If they equal each other BUT the first value isn't 1, return 1
                    elif A[i] == j and A[0] != 1:
                        #print("Not at the end of the list but the start of the list isn't 1")
                        return 1
                    else:
                        #print("Should be returning j here first loop")
                        return j
                elif i == (len(A) - 1):
                    #End of the list, and the first value is 1
                    if A[i] == j and A[0] == 1:
                        #print("You have reached the end of the list")
                        maxList = len(A) - 1
                        j = A[maxList] + 1
                        return j
                    #End of the loop but the first value isn't 1
                    elif A[i] == j and A[0] != 1:
                        #print("End of the list and the list is not 1")
                        return 1
                    else:
                        #print("Should be returning J here second loop")
                        return j