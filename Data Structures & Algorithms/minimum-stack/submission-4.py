class MinStack:

    def __init__(self):
        self.stack = []
        self.support=[]
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.support.append(val)
            self.stack.append(val)
            return 
        self.stack.append(val)
        mini=self.support[-1]
        if val < mini:
            self.support.append(val)
        else:
            self.support.append(mini)

    def pop(self) -> None:
        self.support.pop()

        self.stack.pop()

        
        

    def top(self) -> int:
        return self.stack[-1]
       
        

    def getMin(self) -> int:
        return self.support[-1]
        
        
