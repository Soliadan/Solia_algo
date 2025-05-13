class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_key = False


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_key = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_key

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


def trie_from_patterns(patterns: list[str]) -> TrieTree:
    trie = TrieTree()
    for word in patterns:
        trie.insert(word)
    return trie

if __name__= "__main__":
    patterns = ["apple", "ape", "apex", "bat", "ball"]

    trie = trie_from_patterns(patterns)

    print(trie.search("apple"))     
    print(trie.search("apples"))    
    print(trie.starts_with("ap"))   
    print(trie.starts_with("ba"))   
    print(trie.starts_with("cat"))  