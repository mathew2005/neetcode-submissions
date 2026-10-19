# {
#     1: [0,2,]
#     2: [3,4]
#     3:[1]
# }

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make the adjacency list
        adjList = {i: [] for i in range(numCourses)}
        for cou,pre in prerequisites: adjList[cou].append(pre)
        visiting = set()
        
        def dfs(crs):
            nonlocal visiting
            if not adjList[crs]:
                return True
            if crs in visiting:
                return False
            visiting.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre): return False
            adjList[crs] = []
            return True
                
        
        for crs in range(numCourses):
            if not dfs(crs): return False
            visiting = set()
        return True
        
        
        