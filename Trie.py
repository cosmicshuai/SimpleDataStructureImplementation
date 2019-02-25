from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.is_word = True
    
    def search(self,word):
        cur = self.root
        for char in word:
            cur = cur.children.get(char,None)
            if cur is None:
                return False
        return cur.is_word
    
    def startWith(self,prefix):
        cur = self.root
        for char in prefix:
            cur =  cur.children.get(char,None)
            if cur is None:
                return False
        return True
