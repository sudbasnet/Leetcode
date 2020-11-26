class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        we most definitely need to use a hash table to find out the position of the 
        same letter last seen.
        
        abcdecxyzc.....
              ^  ^
              s  e
        we are looking at two points (start, end) 
        so make two pointers.
        
        start and end pointers. start pointer stays put until we see a seen letter
        then start changes, to lastseen + 1, so the new length is end - start + 1
        
        store the last location of each letter. only look for duplicates from the start
        point or later
        
        """
        if len(s) <= 1:
            return len(s)
        
        seenChars = {}
        start = 0
        longestSubstringLen = 0
        
        for end in range(len(s)):
            if s[end] in seenChars and seenChars[s[end]] >= start:
                start = seenChars[s[end]] + 1
            seenChars[s[end]] = end
            longestSubstringLen = max(longestSubstringLen, end - start + 1)
        
        return longestSubstringLen