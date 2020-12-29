import collections
import queue

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        seeing a bi-directional graph here
        
        a * path value = b 
        
        
        a/b = 1.5 ?? means a = b * 1.5
        
        so the path from a to b: a -> 1.5 -> b
        and the path from b to a : b -> 1/1.5 -> a
        
        data structure
        {
        a: {b: 1.5, c: xx, ...}
        b: {a: 1/1.5, c: xxx, ...}
        
        
        [["a","b"],["b","c"]], values = [2.0,3.0]
        {
        a : {b: 2.0}, 
        b : {a: 0.5, c: 3.0},
        c : {b: 0.33}
        }
        '''
        
        graph = collections.defaultdict(dict)
        for equation, value in zip(equations, values):
            a, b = equation
            nodeA, nodeB = graph[a], graph[b]
            nodeA[b], nodeB[a] = value, 1/value
        
        results = []
        for nodeA, nodeB in queries:
            if nodeA not in graph or nodeB not in graph:
                results.append(-1.0)
            else:
                q = queue.Queue()
                q.put([nodeA, 1])
                visited = [nodeA]
                while not q.empty():
                    node, cost = q.get()
                    visited.append(node)
                    if node == nodeB:
                        results.append(cost)
                        break
                    for n, c in graph[node].items():
                        if n not in visited:
                            q.put([n, c * cost])
                if node != nodeB:
                    results.append(-1.0)
        
        return results
                    