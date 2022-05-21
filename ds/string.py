""" Intro
A string is a sequence of characters.
Tips for array apply to strings.
"""


""" Common
data structures for looking up strings:
    - Trie/prefix tree
    - Suffix tree
Algos:
    - Rabin Karp for efficient searching of substring with rolling hash
    - KMP for efficient searching of substring
"""


""" TC
Access: O(1)
Search: O(n)
Insert: O(n)
Remove: O(n)

Find substrng: O(n.m) (KMP is more efficient)
Concatenating strings: O(n+m)
Slice: O(m)
Split by token: O(m)
Strip (remove leading / trailing whitespace): O(n)
"""


""" Things to clarify
Input char set
case sensitivity
empty string
string with 1/2 chars
string with repeated chars
string with distinct chars
"""


""" Techniques
Counting chars
- Use hash table / map. Python: collections.Counter
- Space complexity for keeping a couner is O(1) instead of O(n)!
    since there is only 26 char in input set, for e.g.

String of unique chars
- masks

Anagram
- frequency counting

Palindrome
- reverse the string and it should be equal to itself
"""