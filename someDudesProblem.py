# long string came from n grades, each grade was 0 - 100, 
# return max avg possible

# this function always returns a list, you can optimize it
# hint for optimization: instead of returning an array, compare the best result so far,
#                        update the best result if what you receive is greater.
#                        initialize as 0, return negative infinity if invalid string.
def continueSearching(inputString, n, runningSum, runningCount):
    # if we have reached the end of string, and gotten grades for everyone
    if n == 0 and len(inputString) == 0:
        # return the value in a list
        return [runningSum/runningCount]

    # if we are either out of inputString or out of students to assign grades to
    elif n == 0 or len(inputString) == 0:
        # returns empty array / list
        return []
    
    # define a list / array that will hold the values of all the averages
    averages = []

    # only valid number of length 3 is 100, so if the first 3 letters are '100' we consider it
    if len(inputString) >= 3 and inputString[:3] == '100':
        averages += continueSearching(inputString[3:], n - 1, runningSum + 100, runningCount + 1)

    # if the first number is not 0 that means we can also consider the first 2 digits 
    if len(inputString) >= 2 and inputString[0] != '0':
        averages += continueSearching(inputString[2:], n - 1, runningSum + int(inputString[:2]), runningCount + 1)

    # finally we will always consider the first digit as a grade
    averages += continueSearching(inputString[1:], n - 1, runningSum + int(inputString[0]), runningCount + 1)

    # returns an array / list
    return averages


# main function
def averageGrades(inputString, n):
    #  at each point, what are my options ??
    #  every time we recurse, we need to pass the "sum so far" and the "count so far"
    allPossibleAverages = continueSearching(inputString, n, runningSum=0, runningCount=0)
    return max(allPossibleAverages + [0])


# print("00000")
print(averageGrades("00000", 5))
print()
print("01001001")
print(averageGrades("01001001", 5))
print()
print("100100100100100")
print(averageGrades("100100100100100", 5))
print()
print("10099100990")
print(averageGrades("10099100990", 5))