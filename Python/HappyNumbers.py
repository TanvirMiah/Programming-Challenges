"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

def isHappy(self, n):
    complete = False
    intToList = [int(n) for n in str(n)]
    while complete == False:
        total = 0
        for i in range(0, len(intToList)):
            total += (intToList[i])**2
            print(total)
        if total == 1:
            print(n, " is a happy number")
            complete = True
            return True
        else:
            intToList = [int(total) for total in str(total)]
            
#Known Issue: goes into infinite loop when a number isn't happy