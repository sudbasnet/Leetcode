def decimalToBinaryArray(num):
    binArray = []
    if num > 1: 
        binArray += decimalToBinaryArray(num // 2) 
    return binArray + [num % 2]

def decimalToBinaryNumber(num):
    binNum = 0
    if num > 1: 
        binNum = binNum * 10 + decimalToBinaryNumber(num // 2) 
    return binNum * 10 + (num % 2)

print(decimalToBinaryArray(8))
# [1, 0, 0, 0]

print(decimalToBinaryNumber(8))
# 1000