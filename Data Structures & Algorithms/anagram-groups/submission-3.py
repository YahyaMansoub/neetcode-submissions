class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mpp = {}
        counter = [0]*26

        for s in strs:
            for ch in s:
                counter[ord(ch)-ord('a')]+=1
            key = tuple(counter)
            counter = [0]*26

            if key in mpp:
                mpp[key].append(s)
            else:
                mpp[key]=[s]

        res = [arr for arr in mpp.values()]

        return res

            
        
        
        
        
        
    