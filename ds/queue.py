""" Intro
A queue is a linear collection of elements that are maintained 
in a sequence and can be modified by the addition of elements at 
one end of the sequence (enqueue operation) and the removal of 
elements from the other end (dequeue operation). 

Usually, the end of the sequence at which elements are added is 
called the back, tail, or rear of the queue, and the end at 
which elements are removed is called the head or front of 
the queue. 

As an abstract data type, queues can be implemented using arrays 
or singly linked lists.

This behavior is commonly called FIFO. 

Breadth-first search is commonly implemented using queues.
"""


""" Python implementation
queue
"""


""" TC
O(1) for enqueue/offer, dequeue/poll, front, back, isEmpty
"""


""" Things to look out for
Most languages don't have a built in Queue class which to be used, 
and candidates often use python lists as a queue. 
However, the enqueue operation in such a scenario will be O(n)
because it requires shifting of all other elements by one. 

In such cases, you can flag this to the interviewer and say 
that you assume that there's a queue data structure to use 
which has an efficient enqueue operation.
"""


""" Corner cases
empty / 1-item / 2-item queues
"""