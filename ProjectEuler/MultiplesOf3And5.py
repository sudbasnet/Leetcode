"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

def multiples3And5(below: int):
    #O(n) would be go through all the numbers and then add it
    multipleSum = 0
    upto = below - 1
    multiplesOfThree = upto//3 # 333
    multiplesOfFive = upto//5 # 199

    for num in range(1, multiplesOfThree + 1):
        multipleSum += (3 * num)
        # since multiplesOf5 will always be less
        # check if the number is not 3's multiple
        if num <= multiplesOfFive and (5*num)%3 != 0:
            multipleSum += (5 * num)

    return multipleSum

def multiples3And5_(below: int):
    multipleSum = 0
    n = 1
    while n < below:
        if n%3 == 0 or n%5 == 0:
            multipleSum += n
        n += 1
    return multipleSum


def bestSolution(below):
    # sum of first n natural numbers 
    # (n * (n + 1))/2
    upto = below - 1
    multiplesOfThree = upto//3 # 333
    # this means we have to do
    # 3 * 1 + 3 * 2 + ... + 3 * 333
    # of 3 * (1 + 2 + ... + 333)

    multiplesOfFive = upto//5 # 199
    # similarly we are doing
    # 5 * (1 + 2 + ... + 199)

    # obviously we need to discard some thing 
    # that might be duplicated, like numbers
    # divisible by bot h 3 and 5 or num divisible
    # by 15. so we do the same for 15
    multiplesOfFifteen = upto//15 # 66

    # summation of multiples of 3 is
    multipleSum3 = (multiplesOfThree * (multiplesOfThree + 1))//2
    # summation of multiples of 5 is 
    multipleSum5 = (multiplesOfFive * (multiplesOfFive + 1))//2
    # summation of multiples of 15 is
    multipleSum15 = (multiplesOfFifteen * (multiplesOfFifteen + 1))//2

    # so the final answer is
    return 3*multipleSum3 + 5*multipleSum5 - 15*multipleSum15

print("linear")
start = time.time()
print(multiples3And5_(1000000))
print(time.time() - start)
print()
print("slightly optimized")
start = time.time()
print(multiples3And5(1000000))
print(time.time() - start)
print()
print("constant time")
start = time.time()
print(bestSolution(1000000))
print(time.time() - start)

# linear
# 233333166668
# 0.0967719554901123

# slightly optimized
# 233333166668
# 0.08377575874328613

# constant time
# 233333166668
# 0.0