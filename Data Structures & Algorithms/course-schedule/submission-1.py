class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        q = deque()
        
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            indegree[c1]+=1
        for c in range(len(graph)):
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

        return len(res)==numCourses
            
        