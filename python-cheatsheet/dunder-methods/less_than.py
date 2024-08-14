class Pair:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        return (self.freq < other.freq) or (self.freq == other.freq and self.word > other.word)

    def __repr__(self):
        return f"(freq={self.freq}, word={self.word})"


if __name__ == '__main__':
    fw1 = Pair(2, "the")
    fw2 = Pair(3, "bcd")
    fw3 = Pair(2, "boy")
    lst = [fw1, fw2, fw3]
    lst.sort()
    print(lst)
