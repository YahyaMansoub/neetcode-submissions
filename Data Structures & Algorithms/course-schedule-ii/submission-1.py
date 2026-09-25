class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        q = deque()

        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for c1 ,c2 in prerequisites:
            graph[c2].append(c1)
            indegree[c1]+=1

        for c in range(numCourses):
            if indegree[c]==0:
                q.append(c)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)

            for c in graph[curr]:
                indegree[c]-=1
                if indegree[c]==0:
                    q.append(c)

        if len(res)==numCourses:
            return res
        else:
            return []