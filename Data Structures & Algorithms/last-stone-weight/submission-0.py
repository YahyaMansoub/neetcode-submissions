class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)

        for i in stones: 
            heapq.heappush(maxHeap,-i)

        while len(maxHeap)>=2:
            val1=-heapq.heappop(maxHeap)
            val2=-heapq.heappop(maxHeap)
            if val1==val2:
                continue
            else:
                heapq.heappush(maxHeap, val2-val1)


        if len(maxHeap)==1:
            return -heapq.heappop(maxHeap)
        else:
            return 0
            