'''
[a,b] means that you must take course b before course a
numCourses you have to take -> labeled from course 0 to course numCourses - 1
True if you can finish all courses, False if can't
We need to detect for any cycles by using labels

Contraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.

Steps:
1. Map each course to its pre reqs
2. Have Unvisited, Visiting, Visited indicators 0, 1, 2
3. Perform DFS on each of the prereq's and mark them as visited
4. If you are on a node that is already marked as 1, return false
5. After visiting mark 2
6. The dfs function will return true or false, and then we return that

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        # full adjacency list mapping 
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)
        
        # Indicators
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        # change the states at the nodes
        def dfs(course):
            state = states[course]
            # base cases - cycle or valid
            if state == VISITING:
                return False
            if state == VISITED:
                return True
            # mark the course we are on as visiting
            states[course] = VISITING
            
            for neighbor in prereqs[course]:
                if not dfs(neighbor):
                    return False
            # only if all the prereq's are chill and no cycles (VISITING) in path
            states[course] = VISITED
            return True
        
        # pass in the course to dfs function
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True















