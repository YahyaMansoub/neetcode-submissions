class TimeMap:

    def __init__(self):
        
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((value, timestamp))
            
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        i, j = 0, len(arr)-1
        res = ""
        while i<=j:
            mid = (i+j)//2

            if arr[mid][1]<=timestamp:
                res = arr[mid][0]
                i=mid+1

            else:
                j=mid-1

        return res 

