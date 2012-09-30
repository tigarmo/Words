from tree import WordTree


def main():
    with open("/usr/share/dict/words", 'r') as f:
        l = []
        for line in f:
            l.append(line.strip())

    wt = WordTree()
    for line in l:
        wt.addWord(line)

    while True:
        print "Enter a letter combination:"
        s = raw_input().strip()
        words = wt.allWords(s)
        for w in words:
            print "> " + w

if __name__ == "__main__":
    main()
