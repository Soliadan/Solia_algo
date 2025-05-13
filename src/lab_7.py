class TrieNode:
    """Вузол Trie"""
    def __init__(self):
        self.children = {}
        self.is_key = False


class TrieTree:
    """Trie (префіксне дерево)"""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Додає слово до Trie"""
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_key = True

    def search(self, word: str) -> bool:
        """Шукає повне слово"""
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_key

    def starts_with(self, prefix: str) -> bool:
        """Перевіряє наявність слів із вказаним префіксом"""
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


def trie_from_patterns(patterns: list[str]) -> TrieTree:
    """Створює Trie з переданого списку слів"""
    trie = TrieTree()
    for word in patterns:
        trie.insert(word)
    return trie

if __name__= "__main__":
    patterns = ["apple", "ape", "apex", "bat", "ball"]

    trie = trie_from_patterns(patterns)

    print(trie.search("apple"))     # True
    print(trie.search("apples"))    # False
    print(trie.starts_with("ap"))   # True
    print(trie.starts_with("ba"))   # True
    print(trie.starts_with("cat"))  # False