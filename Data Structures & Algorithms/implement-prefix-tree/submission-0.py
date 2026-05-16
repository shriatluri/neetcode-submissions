'''
They key here is the hashmap as the keys will be the letters on the level
the values will be other trie nodes that the letter goes to
Ex: for CAT, {C: node} -> {A:node} etc. 
they keys in a dict will have the same parent and be on the same level
'''
# TrieNode will have it's children in a hashmap and then end of word or not
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False # needed to differentiate word and prefix

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    # insert a word
    def insert(self, word: str) -> None:
        # start at root
        cur = self.root
        for c in word:
            if c not in cur.children:
                # add it to children
                cur.children[c] = TrieNode()
            # we move to next letter
            cur = cur.children[c]
        # set the end of word to true at the last TrieNode()
        cur.endOfWord = True

    # seach for a word
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # return endOfWord
        return cur.endOfWord

    # just check starts with
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        