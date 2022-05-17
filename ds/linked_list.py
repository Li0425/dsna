""" Intro
Like array, used to represent sequential data

Linear collection of data whose order isn't given by their physical
placement in the memory, as opposed to arrays (data stored in
sequential blocks of memory).

Each node in linked list stores data, & an address of the next element 
(a reference, the 'link').
Linked list is a data structure consisting a collection of notes
which represent a sequence together.

+: insertion & deletion of elements is O(1) whereas in arrays the
    the following elements need to be shifted
-: access time is O(n) as need to traverse from the start.
    Cannot access via index like array
    Search time is O(n) too.
"""


""" Types of LL
Singly linked lists: each node points to the next node,
    last node points to null
Doubly linked lists: each node has two pointers, prev, next.
    the prev pointer of 1st node and next pointer of last node
    point to null
Circular linked lists: singly linked list where the last node
    points to the 1st node. OR Doubly linked list where
    prev of 1st node points to last node, next of last node
    points to 1st node
"""


""" Common routines
1. Count the num of nodes
2. Reverse a LL in-place
3. Finding the middle node of the linked list using 2 pointers (fast/slow)
4. Merge 2 LLs
"""


""" Corner cases
1. Empty LL (head is null)
2. Single node
3. 2 nodes
4. LL with cycles. Clarify if there might be cycles in the LL.
    Usually no, and don't need to handle them in the code
"""


""" Techniques
1. Add dummy node at head and/or tail to avoid handling edge cases
    where operations are to be performed at head/tail
    Dummy node ensures ops will never be done on the head or tail,
    hence removing the many conditional checks for null pointers.
    Remember to remove dummies at the end of operation.
2. Have 2 pointers. Approached used in many classic linked list problems
    (i) Getting the kth from last node - Have two pointers, 
    where one is k nodes ahead of the other. When the node ahead 
    reaches the end, the other node is k nodes behind
    (ii) Detecting cycles - Have two pointers, where one pointer
    increments twice as much as the other, if the two pointers meet,
    means that there is a cycle
    (iii) Getting the middle node - Have two pointers, where one 
    pointer increments twice as much as the other. When the 
    faster node reaches the end of the list, the slower node 
    will be at the middle
3. Space: many linked list problems can be easily solved by creating
    a new linked list and adding nodes to the new linked list 
    with the final result. However, this takes up extra space 
    and makes the question much less challenging. The interviewer 
    will usually request that you modify the linked list in-place 
    and the solve the problem without additional storage. 
    You can borrow ideas from the Reverse a Linked List problem.
4. Elegant modification ops. LL's non-sequential nature of memory
    allows for efficient content modification. In array, you can
    only modify value at a position. In LL, you can edit pointer.
    This makes truncating LL easy (make next null)
    Combining two lists - attach the head of the second list to
        the tail of the first list
    Swapping values of nodes - Just like arrays, just swap the value
    of the two nodes, there's no need to swap the next pointer
"""


""" Coding problems
- Reverse linked list
"""