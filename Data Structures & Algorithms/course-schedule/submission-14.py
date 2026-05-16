from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edgeList = defaultdict(list)

        for a, b in prerequisites:
            edgeList[b].append(a)

        visited = [False] * numCourses
        inPath = [False] * numCourses

        def dfs(node: int) -> bool:
            if visited[node]:
                return False
            
            if inPath[node]:
                return True
            
            inPath[node] = True

            for nei in edgeList[node]:
                if dfs(nei):
                    return True
            
            # recursion 
            visited[node] = True
            inPath[node] = False
        
        for course in range(numCourses):
            if not visited[course]:
                if dfs(course):
                    return False
        
        return True
                    



