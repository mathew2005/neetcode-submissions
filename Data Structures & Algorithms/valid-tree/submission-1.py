from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        isTree = True
        visited = set()
        adjList = defaultdict(list)
        for parent,child in edges: adjList[parent].append(child); adjList[child].append(parent)
        def dfs(parent,node):
            nonlocal isTree
            if node in visited:
                return
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    isTree = False                
                dfs(node,neighbor)
        dfs(-1,0)
        print(isTree,visited)
        return isTree and len(visited) == n