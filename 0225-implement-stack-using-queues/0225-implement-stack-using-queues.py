class MyStack:

    def __init__(self):
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)
        

    def pop(self) -> int:
        return self.items.pop()
        

    def top(self) -> int:
        return self.items[-1]
        

    def empty(self) -> bool:
        return self.items == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()