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
		print "Enter a word:"
		s = raw_input().strip()
		if wt.isWord(s):
			print s + " IS a word."
		else:
			print s + " IS NOT a word."

if __name__ == "__main__":
	main()

