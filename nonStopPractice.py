
# unique email address
from _typeshed import FileDescriptor


def uniqueEmailAddresses(emails):
    validEmails = set()
    for email in emails:
        validEmail = []
        stopRecording = False
        for i in range(len(email)):
            if email[i] == '+':
                stopRecording = True
            elif email[i] == '@':
                validEmails.add(''.join(validEmail)+email[i:])
                break
            elif email[i] == '.':
                continue
            if not stopRecording: validEmail.append(email[i])
    return len(validEmails)


# OddEvenJump
# input arr, Jumps from 1st, 3rd, 5th, ... jumps are called odd jumps
# 2nd, 4th, 6th jumps are called even Jumps. (Note its not the index but the xth jump)
# in Odd you can jump to another index, with a value higher or equal to yourself but it has to be the lowest value higher than yourself
# in Even jump you can jump to another index with a value lower or equal to yourself, but its has to he highest among the low values
# you can only jump to the right, sometimes there are no valid jumps

# starting index is good if from a starting index, you can reach the end

def oddEvenJump(arr):
    # the last element is good for both even and odd
    # check if the previous element in the array can reach this place by making a odd jump or even jump
    
    # for each index I need to know what the next highest is
    # for each index I need to know what the next lowest is
    # sort them first, then create a monotonic stack
    # [-1, 1], [0, 3], [2, 2]
    # [1, 0, ] save the stack always in decending order
    if len(arr) <= 1:
        return len(arr)

    def getNextBigNumber(arr):
        result = [-1 for _ in arr]
        sortedArr = sorted([[a, i] for i, a in enumerate(arr)])
        mStack = []
        for _, i in enumerate(sortedArr):
            while mStack and mStack[-1] <= i:
                result[mStack.pop()] = i
            else:
                mStack.append(i)
        return result
    
    def getNextSmallNumber(arr):
        result = [-1 for _ in arr]
        sortedArr = sorted([[-a, i] for i, a in enumerate(arr)])
        mStack = []
        for _, i in enumerate(sortedArr):
            while mStack and mStack[-1] <= i:
                result[mStack.pop()] = i
            else:
                mStack.append(i)
        return result

    canJump = [{'odd': False, 'even': False} for _ in range(len(arr)-1)]
    canJump.append({'odd': True, 'even': True})

    nextSmall = getNextSmallNumber(arr)
    nextBig = getNextBigNumber(arr)

    goodStarts = 1

    i = len(arr) - 2
    while i >= 0:
        canJump[i]['even'] = True if (nextSmall[i] > i and canJump[nextSmall[i]]['odd']) else False
        canJump[i]['odd'] = True if (nextBig[i] > i and canJump[nextBig[i]]['even']) else False
        if canJump[i]['even'] or canJump[i]['odd']:
            goodStarts += 1
        i -= 1

# License key Formatting
"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes. 
The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, 
except for the first group which could be shorter than K, but still must contain at least one character. 
Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.
"""
def licenseKeyFormatting(S, K):
    '''
    result = list[str]
    len(S)%K 
    if this is 0, its equally divided else pluck out that many letters, set the starting index to this num
    string.upper()
    '''
    S = S.replace('-', '')
    result = []

    first = len(S)%K
    if first > 0: result.append(S[:first].upper())

    counter = 1
    start = first
    for i in range(first, len(S)):
        if counter % K == 0:
            result.append(S[start:i+1].upper())
            start = i+1
        counter += 1

    return '-'.join(result)

"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
[
    "ball",
    "area",
    "lead",
    "lady"
]
"""
import collections

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current: current[letter] = {}
            current = current[letter]
        current['word'] = word

    def fetchAllWithPrefix(self, prefix):
        results = []
        current = self.root
        for pre in prefix:
            if pre not in current:
                return []
            current = current[pre]
        
        stack = [current]
        while stack:
            current = stack.pop()
            if 'word' in current: 
                results.append(current['word'])
            for k, val in current.items():
                if k != 'word': stack.append(val)
        return results

def wordSquares(words):
    ''' need to use a TRIE data structure '''
    trie = Trie()
    for word in words:
        trie.insert(word)
    boxes = []

    def makeBox(box):
        if len(box) == len(box[0]):
            boxes.append(box)
            return
        prefix = ""
        for i, b in enumerate(box):
            prefix += b[i+1]
        for nextWord in trie.fetchAllWithPrefix(prefix):
            makeBox(box + [nextWord])

    for word in words:
        makeBox([word])


"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
"""
# Word Search II
# 
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current: current[letter] = {}
            current = current[letter]
        current['word'] = word

    def nextLetter(self, prefix):
        current = self.root
        for pre in prefix:
            if prefix not in current:
                return []
            current = current[pre]
        return [k for k in current.keys() if k != 'word']

def findWords(board, words):
    output = []
    trie = Trie()
    for word in words: trie.insert(word)\
    
    def traverse(prefix, start, visited):
        if prefix in words:
            output.appen(prefix)

        r, c = start
        prefix += board[r][c]
        nextLetters = trie.nextLetter(prefix)
        invalidRC = r < 0 or c < 0 or r >= len(board) or c >= len(board[0])
        if invalidRC or not nextLetters:
            return
        
        if (r-1,c) not in visited: traverse((r-1, c), visited + [(r, c)])
        if (r+1,c) not in visited: traverse((r+1, c), visited + [(r, c)])
        if (r,c-1) not in visited: traverse((r, c-1), visited + [(r, c)])
        if (r,c+1) not in visited: traverse((r, c+1), visited + [(r, c)])

        

