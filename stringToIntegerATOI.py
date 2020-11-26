class Solution:
    def myAtoi(self, s: str) -> int:
        """
        first step would be to left trim the input
        multiplyBy = 1 if first letter is not '-' else -1
        have a runningNum
        go letter by letter, if isdigit else stop
        
        maxNum = some number
        runningNum * 10 + newDigit%10 >= maxNum
        runningNum >= (maxNum - newDigit%10)//10
        
        if out of bounds we return the min or max
        """
        cleanStr = s.lstrip()
        
        if len(cleanStr) == 0:
            return 0
            
        multiplyBy = 1 
        if cleanStr[0] == '-' and len(cleanStr) > 1:
            multiplyBy = -1
            cleanStr = cleanStr[1:]
        elif cleanStr[0] == '+' and len(cleanStr) > 1:
            cleanStr = cleanStr[1:]
            
        maxNum = (2**31) - 1
        minNum = -2**31
        runningNum = 0
        
        for i in range(len(cleanStr)):
            if cleanStr[i].isdigit():
                if runningNum > (maxNum - int(cleanStr[i])%10)//10:
                    return minNum if multiplyBy < 0 else maxNum
                else:
                    runningNum = runningNum * 10 + int(cleanStr[i])
            else:
                break
        
        return runningNum * multiplyBy
        
        
        