class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)

        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap) 

        cooldown = deque()

        time = 0

        while maxHeap or cooldown:
            time +=1

            if maxHeap:
                count = heapq.heappop(maxHeap)
                count +=1

                if count != 0:
                    cooldown.append((count, time+n))

            if cooldown and cooldown[0][1] == time:
                count, readyTime = cooldown.popleft()
                heapq.heappush(maxHeap, count)
        
        return time 
        

                
        

