# I am in the lowest 5% of the fastest solutions.
# I dont know how to solve it faster than this
# maybe I could just decrease the size of the main stones array once I've seen an index



def toTuple(listItem):
    return (listItem[0], listItem[1])

def findOneNeighbor(stones, fromCoordinate, visited):    
    for stone in stones:
        sharesColumnOrRow = (stone[0] == fromCoordinate[0] or stone[1] == fromCoordinate[1])
        if not visited[toTuple(stone)] and sharesColumnOrRow:
            return stone
    return

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        You cannot make a move if a stone does not share a row or col 
        with another stone
        
        I can see from a little bit of scribbling that the stone with the most 
        neighbors (more elements in its row or col) should be removed last
        
        so we might need to go through the list and assign neighbors to each stone???
        
        if a stone is already included in someone else's set, then dont make a group for 
        them???
        
        maybe do a dfs, find all stones that are in the same row and col and are in same 
        row and col of the next element??? DFS can give you the entire list, but we still need to 
        know which one has the least number of neighbors ????
        
        the first one could be the one that could be removed. How do we know that? we cannot know that
        so what do we do?? do we track the number of neighbors too?? arrange them in descending order,
        then remove the one with the least neighbor first???? if all neighbors of a stone is gone, 
        then I cannot remove a stone.
        
        make a dictionary, put each's neighbors in the dict
        start from the one with the lowest neighbors, delete each neighbor one by one.
        """
        
        
        # lets do a DFS and find all the connected components
        # every time you backtrack you remove a component :)
    
        if len(stones) <= 1:
            return 0
        
        visited = {}
        for i in range(len(stones)):
            visited[toTuple(stones[i])] = False
        
        stack = []
        moves = 0 
        
        for stone in stones:
            if not visited[toTuple(stone)]:
                stack.append(stone)
                
            while stack:
                currentNode = stack[-1] # peek
                visited[toTuple(currentNode)] = True
                neighbor = findOneNeighbor(stones, currentNode, visited)
                if neighbor:
                    # just pull one of the neighbors
                    stack.append(neighbor)
                else:
                    stack.pop()
                    if stack:
                        # meaning there's still stuff in the stack
                        # remember you cannot make a move if a stone
                        # has no neighbors left
                        moves += 1
        return moves
                    
            
            
        
        
        