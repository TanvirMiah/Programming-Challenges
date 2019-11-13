"""
Given an array of coins and the total value of change, output the fewest amount of coins required to make the change
"""

def minCoins(A, T):
    A.sort(reverse=True)
    #print("A reversed is: ", A)
    totalCoins = 0
    complete = False
    totalLength = len(A)
    currentPos = 0
    while currentPos < totalLength:
        while complete == False:
                #print("Current coin in questions is: ", A[currentPos], "And T is: ", T)
                if T == 0:
                    complete = True
                    return totalCoins
                elif T >= A[currentPos]:
                    T = T - A[currentPos]
                    #print("T has been reduced. T is currently ", T)
                    totalCoins += 1
                    #print("Total coin value has increased. It is ", totalCoins)
                elif T < A[currentPos]:
                    currentPos += 1 