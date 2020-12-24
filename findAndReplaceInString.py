class Solution:
    def findReplaceString(self, S: str, indexes: [int], sources: [str], targets: [str]) -> str:
        ''' Dont jump to code '''
        ''' 
        Put the problems in the same list or tuple and sort by the indexes.
        Once you have that go through the combined list, make the updates 
        but also track by how much the updated string shifts everytime.
        '''
        updatedStr = S
        shiftsBy = 0

        for i, source, target in sorted(zip(indexes, sources, targets)):
            if S[i:i+len(source)] == source:
                updatedStr = updatedStr[:shiftsBy+i] + \
                    target + updatedStr[shiftsBy+i+len(source):]
                shiftsBy += len(target) - len(source)
                
        return updatedStr
