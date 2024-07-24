import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)  # self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('checker')
    trie.insert('checked')
    trie.insert('cat')
    in_trie = trie.search('checked')
    print('searched for word checked: ', in_trie)
    in_trie = trie.search('check')
    print('searched for word check: ', in_trie)
    prefix_in_trie = trie.starts_with('chec')
    print('starts with chec:', prefix_in_trie)
    prefix_in_trie = trie.starts_with('checke')
    print('starts with checke:', prefix_in_trie)
    prefix_in_trie = trie.starts_with('checkf')
    print('starts with checkf:', prefix_in_trie)
