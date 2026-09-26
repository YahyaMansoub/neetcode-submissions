from math import ceil 


def get_h(k, piles ):
    curr = 0
    for i in piles:
        curr+=ceil(i/k)
    return curr 

class Solution:

    


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        S = sum(piles)
        max_pile = max(piles)

        max_k =ceil(max_pile/h) 

        i, j = 1, S
        res = -1 
        while i <= j:
            mid = (i+j)//2
            if get_h(mid, piles)<= h:
                j=mid-1
                res = mid 
            else: 
                i=mid+1
            

        return res
