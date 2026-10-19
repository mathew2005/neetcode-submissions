class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {num: [] for num in range(numCourses)}
        for cou,pre in prerequisites: adjList[cou].append(pre)
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if not adjList[crs]:
                return True
            
            visiting.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre): return False
            visiting.remove(crs)
            adjList[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
        