class TrieNode:
    def __init__(self, val=0):
        self.val = val
        self.child = set()

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.child = set()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in [ele.val for ele in curr_node.child]:
                curr_node.child.add(TrieNode(c))
            else:
                for ele in curr_node.child:
                    if ele.val == c:
                        curr_node = ele

    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            if c not in [ele.val for ele in curr_node.child]:
                return False
            else:
                for ele in curr_node.child:
                    if ele.val == c:
                        curr_node = ele
        return True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix)