""" Intro
Arrays hold values of the same type at contiguous memory locations.
Concern about 2 things: position/idex of an element & element itself.

In Python, 
    arrays are lists (values could be diff types)
    size is dynamic

+: store multiple elements of the same type with 1 single variable name
+: access elements is fast if index is known, 
    as opposed to LL where traversal from head is needed
-: Addition and removal of elements into/from the middle of an array is slow 
    because the remaining elements need to be shifted to accommodate it. 
    An exception to this is if the position is at the end of the array.
-: if array size is fixed (in certain language) after initialization,
    insertion may require a nre array and transferring elements takes O(n)
    
Both arrays and strings (array of chars) are sequences. Techniques are shared.
"""


""" Terms
- Subarray: a range of contiguous values
- Subsequence: a subgroup of values that sequence is preserved
"""


""" Time complexity
Access: O(1)
Search: 0(n) if unsorted, O(log(n)) if sorted
Insert: O(n) or O(1)
Remove: O(n) or O(1)
"""


""" Be careful
- Duplicated values
- Go out of bounds
- Slicing / concatenating arrays, which would take O(n) time.
    Use start/end indices to demarcate a subarray/range where possible
"""


""" Corner cases
- empty sequence
- cases with 1 or 2 elements
- cases with duplicated elements
- duplicated values in the sequence
"""


""" Techniques
(1) Sliding window
2 pointers usually move in the same direction that will not overtake each other
This ensures every value is visited at most twice, TC is still O(n)

(2) 2 pointers
a more general version of sliding window where the pointers can cross each other
and can be on different arrays.
When you are given 2 arrays, it's common to have one pointer (idx) per
array to traverse/compare both, incrementing one of the pointers when relevant

(3) Travers from the right

(4) Sort the array
If the array is sorted or partially sorted, some form of binary search is ppossible
Usually means the interviewer is looking for a solution better than O(n).
Sometimes sorting the arrray first may significantly simply the problem.

(5) Pre-computation
For qns where summation of multiplication of a subarray is involved,
pre-computation using hashing or a prefix/suffix sum/product might be useful

(6) Index has a hash key
If you are given a sequence and interview asks for O(1) space, it
might be possible to use array itself as a hash table.
For example, if the array only has values from 1 to N, where N is len(array),
negate the value at that index (minus one) to indicate presence of that number.

(7) Traverse array more than once
twice/thrice as long as < n times, is still O(n).
May help solve the problem while keeping TC to O(n).
"""
