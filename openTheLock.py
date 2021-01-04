import collections


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """
        looks like a dynamic programming problem.
        string so far --- 
        if the next string makes it a deadlock, then dont do it.

        NOPE!! scratch that, we can use a tree-like structure. Since 
        we are looking for the shortest path, a BFS makes sense here.

        """
        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        moves = {'0': ['1', '9'], '9': ['8', '0']}
        for i in range(1, 9):
            moves[str(i)] = [str(i-1), str(i+1)]

        q = collections.deque()
        q.append('0000')
        deadends.add('0000')
        level, levelItems = 0, 1
        while q:
            current = q.popleft()
            if current == target:
                return level

            for i in range(4):
                move1 = current[:i] + moves[current[i]][0] + current[i+1:]
                move2 = current[:i] + moves[current[i]][1] + current[i+1:]
                if move1 not in deadends:
                    q.append(move1)
                    # need to add to the invalid moves immediately
                    deadends.add(move1)
                if move2 not in deadends:
                    q.append(move2)
                    # need to add to the invalid moves immediately
                    deadends.add(move2)

            levelItems -= 1
            if levelItems == 0:
                levelItems = len(q)
                level += 1
        return -1
