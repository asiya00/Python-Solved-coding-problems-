class Node:
	def __init__(self):
		self.children = {}
		self.endofword = False

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		temp = self.root

		for letter in word:
			if letter not in temp.children:
				temp.children[letter] = Node()
			temp = temp.children[letter]
		temp.endofword = True

	def search(self, word):
		temp = self.roots

		for letter in word:
			if letter not in temp.children:
				return False
			temp = temp.children[letter]

		return temp.endofword

	def startswith(self, prefix):
		temp = self.root

		for letter in prefix:
			if letter not in temp.children:
				return False
			temp = temp.children[letter]
		return True

	def display(self):
		temp = self.root
		print(temp.children)

T = Trie()

T.insert("apple")
T.insert("Banana")
print(T.search("apple"))

print(T.search("app"))


