class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ele_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min_ele_stack:
            curr_min = min(self.min_ele_stack[-1], val)
        else:
            curr_min = val
        self.min_ele_stack.append(curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_ele_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_ele_stack[-1]
