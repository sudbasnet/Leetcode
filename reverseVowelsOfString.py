class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # go from back and front, if both pointers are at vowels, then swap them and move the pointers closer
        # if one is at a pointer and the other is not, then move the one not at a pointer closer
        s = list(s) # ['h', 'e', 'l', 'l', 'o']
        start, end = 0, len(s) - 1
        while start < end:
            if s[start].lower() in vowels and s[end].lower() in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start].lower() in vowels:
                end -= 1
            else:
                start += 1
        return ''.join(map(str, s))
#         # go through the string once and note down the vowels in order 
#         # and also save their indexes
#         vowelsFound = []
#         vowelsAt = []
#         s = list(s)
        
#         # find all vowels and log it
#         for i in range(len(s)):
#             if s[i].lower() in vowels:
#                 vowelsFound.append(s[i])
#                 vowelsAt.append(i)
                
#         # reverse the vowels
#         vowelsFound = vowelsFound[::-1]
        
#         # put the vowels back in
#         for j in range(len(vowelsFound)):
#             s[vowelsAt[j]] = vowelsFound[j]
        
#         # return the string
#         return ''.join(map(str, s))