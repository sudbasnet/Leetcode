<!-- 5. Longest Palindromic Substring -->
First we write a function to tell if a given string is a palindrome, when examined from the center point
```python
def isPalindrome(St: str, pos1: int, pos2: int) -> str:
    i, j = pos1, pos2
    currSubstring = '' 
    while i >= 0 and j < len(St):
        if St[i] != St[j]:
            break
        currSubstring = St[i:j+1]
        i -= 1
        j += 1
    return currSubstring
```
I put two points in the function just to make it usuable for palindromes with median between two (same) letters.
Now, we can write the actual function.

```python
def longestPalindromicSubstring(St):
    longestSubstr = ''
    for i in range(len(St)):
        currSubstr = isPalindrome(St, i, i)
        longestSubstr = longestSubstr if len(longestSubstr) > len(currSubstr) else currSubstr
        if i + 1 < len(St) and St[i] == St[i+1]:
            currSubstr = isPalindrome(St, i, i+1)
            longestSubstr = longestSubstr if len(longestSubstr) > len(currSubstr) else currSubstr
    return longestSubstr


# tests : 
# longestPalindromicSubstring('1b1bb11balppla'), alppla
# longestPalindromicSubstring('1234567890') returns 0
# longestPalindromicSubstring('121'), returns 121
# longestPalindromicSubstring('') returns ''

```

#### More Efficient Solution:
This is someone else's solution
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: # s is already a palindrome
            return s
        maxlen = 1
        start = 0
        for i in range(1, len(s)): # index values of string
            if i - maxlen >= 1:
                temp = s[i - maxlen - 1: i + 1]
                if temp == temp[::-1]:
                    start = i - maxlen - 1
                    maxlen += 2
                    continue
            if i - maxlen >= 0:
                temp = s[i - maxlen: i + 1]
                if temp == temp[::-1]:
                    start = i - maxlen
                    maxlen += 1
        return s[start:start + maxlen]
```

