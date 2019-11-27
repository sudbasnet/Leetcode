### Question
Given a string, find the length of the longest substring without repeating characters.
```
Example 1:
----------
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```
```
Example 2:
----------
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
```
Example 3:
----------
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
### Solution
Have two markers, one is the starting position, and the other is the exploration. Once you see a letter repeated, you change your starting position marker as next to the previous occurance of that letter, *example*: lets say the starting marker is at a and the exploration marker is at 'e'.
```
abcdefgclm
^   ^
 ```
lets say we move forward, and now the exploration marker reaches the second 'c'.
```
abcdefgclm
^      ^
```
Now the starting marker needs to move to the position next to the previous 'c'.
```
abcdefgclm
   ^   ^
```
and now we can continue to explore

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabets = {}
        start, max_length = 0, 0
        for i in range(len(s)):
            if s[i] in alphabets:
                start = max(start, alphabets[s[i]] + 1)
            alphabets[s[i]] = i
            max_length = max(max_length, i - start + 1)
        return max_length
```