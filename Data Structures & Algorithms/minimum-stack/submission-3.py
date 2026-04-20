from collections import deque
class MinStack:

    def __init__(self):
        self.st = deque()
        self.minst = deque()

    def push(self, val: int) -> None:
        if self.minst and self.minst[-1] < val:
            pass
        else:
            self.minst.append(val)
        self.st.append(val)

    def pop(self) -> None:
        if self.minst and self.top() == self.minst[-1]:
            self.minst.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        if self.minst:
            return self.minst[-1]
        else:
            return None

        
