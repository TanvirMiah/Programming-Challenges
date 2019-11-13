#Convert number into the binary format and then out put the largest gap of 0's
#So if the binary output is 100010100, the output would be 3
#If the output binary is 0001 or 1000, the output would be 0

# Binary Gap
def binGap(N):
    print(bin(N))
    return len(max(bin(N)[2:].strip('0').strip('1').split('1')))