""" Intro
hash table is commonly referred to as hash map.
a structure tha map keys to values.
A hash table uses a hash function on an element to compute
    an index, i.e. hash code, into an array of bucket / slots,
    from which the desired value can be found
During lookup, the key is hashed and the resulting hash
indicates where the corresponding value is stored.

Hashing is the most common eg of space-time tradeoff.
Instead of linearly searching an array to determine
if an element is present, O(n), we can traverse once
and hash all elements into a hash table.
Determining if the element is present is a simple 
matter of hashing the element and seeing if it exists
in the hash table, takes O(1) on average.

Hash collision resolution techniques:
- Separate chaining
- Open addressing
"""


""" Python implementation
dict
"""


""" TC
access: not possible as the hash code is not known
Search, insert, remove: O(1)
"""