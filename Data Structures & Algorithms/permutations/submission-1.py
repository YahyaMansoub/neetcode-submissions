class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res, n = [], len(nums)
        test = [False]*n
       

        def bt(curr, seen):

            if len(curr)==n:
                res.append(curr[:])
                return 
                


            for i in range(n):
                if seen[i]:
                    continue 
                else:
                    seen[i]=True 
                    curr.append(nums[i])
                    bt(curr, seen)
                    curr.pop()
                    seen[i]=False
            
        bt([], test)
        return res


