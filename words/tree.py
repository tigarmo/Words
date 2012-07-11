class Node:
	def __init__(self, char = ''):
		self.char = char
		self.children = {}
		self.final = False
	
	def addWord(self,word):
		if not word:
			self.final = True
			return

		c = word[0]
		n = self.children.get(c)
		if not n:
			n = Node(c)
			self.children[c] = n

		n.addWord(word[1:])

	def isWord(self,word):
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

	
	def isWord(self,word):
		return self.head.isWord(word)
