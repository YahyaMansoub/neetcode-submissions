class Solution:
    def isana(a, b):
            return sorted(a)==sorted(b)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mem = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in mem:
                mem[key]=[s]
            else:
                mem[key].append(s)
            
        return list(mem.values())
        
        
        
        
    