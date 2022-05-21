""" Intro
Stack is an abstract data type that supports the operation push
(insert a new element on top of the stack) and pop 
(remove and return the most recently added ele, on top of stack).
LIFO

As an abstract data type, stacks can be implemented using
arrays or singly linked lists.

Stacks are an important way of supporting nested or recursive function
calls and is used to implement depth-first search.
DFS could also be implemented using recursion or a manual stack.

Python implementation: simulated using List
"""


""" TC
top / peek: O(1)
Push, pop: O(1)
isEmpty: O(1)
search: O(n)
"""


""" Corner cases
empty stack, poping from empty stack
stack with 1/2 items
"""