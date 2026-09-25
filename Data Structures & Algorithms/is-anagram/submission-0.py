class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        books, bookt = {}, {}
        for chars, chart in zip(s, t):
            if chars in books:
                 books[chars]+=1
            if chart in bookt:
                bookt[chart]+=1

            if chars not in books:
                books[chars]=1
            if chart not in bookt:
                bookt[chart]=1
        
        return books == bookt

            