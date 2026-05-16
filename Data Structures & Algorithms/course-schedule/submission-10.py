from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: prereq -> course
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [False] * numCourses   # fully processed
        inPath = [False] * numCourses    # currently in recursion stack

        def dfs(node: int) -> bool:
            # If node is in current path → cycle
            if inPath[node]:
                return True   # found cycle
            # If we've already fully processed this node, no cycle from here
            if visited[node]:
                return False

            # Mark node as being in current recursion stack
            inPath[node] = True

            # Visit neighbors
            for nei in graph[node]:
                if dfs(nei):          # if any neighbor leads to a cycle
                    return True

            # Done exploring this node: remove from path, mark as visited
            inPath[node] = False
            visited[node] = True
            return False

        # Need to try DFS from each node (graph can be disconnected)
        for course in range(numCourses):
            if not visited[course]:
                if dfs(course):
                    return False      # cycle found

        return True                   # no cycles anywhere
