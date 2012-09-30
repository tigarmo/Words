import itertools


class Node:
    def __init__(self, char=''):
        self.char = char
        self.children = {}
        self.final = False

    def addWord(self, word):
        if not word:
            self.final = True
            return

        c = word[0]
        n = self.children.get(c)
        if not n:
            n = Node(c)
            self.children[c] = n

        n.addWord(word[1:])

    def isWord(self, word):
        if not word:
            return self.final

        c = word[0]
        n = self.children.get(c)
        if not n:
            return False

        return n.isWord(word[1:])


class WordTree:
    def __init__(self):
        self.head = Node('')

    def addWord(self, word):
        self.head.addWord(word)

    def prettyprint(self):
        s = ""
        n = self.head
        while n:
            s += "-- " + n.char
            if n.children.values():
                n = n.children.values()[0]
            else:
                n = None

        print s

    def isWord(self, word):
        return self.head.isWord(word)

    def allWords(self, letters):
        all_valid_words = []
        for l in xrange(3, len(letters) + 1):
            all_words = itertools.permutations(letters, l)
            all_words = list(unique_everseen(all_words))
            valid_words = [word for word in all_words if self.isWord(word)]
            for i in valid_words:
                all_valid_words.append("".join(i))
        return all_valid_words


def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in itertools.ifilterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element
