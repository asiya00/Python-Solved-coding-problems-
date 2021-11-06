class BST:
	def __init__(self, key):
		self.key = key
		self.lchild = None
		self.rchild = None

	# Insert method
	def insert(self, data):
		if not self.key:
			self.key = data
			return
		if data < self.key:
			if self.lchild:
				self.lchild.insert(data)
			else:
				self.lchild = BST(data)
		else:
			if self.lchild:
				self.lchild.insert(data)
			else:
				self.lchild = BST(data)

	# Search method
	def search(self, data):
		if data == self.key:
			print("Element found")
			return self.key
		if data < self.key:
			if self.lchild:
				self.lchild.search(data)
			else:
				print("Element not found")
				return
		else:
			if self.rchild:
				self.rchild.search(data)
			else:
				print("Element not found")
				return

	# Delete method
	def delete(self, data):
		if not self.key:
			print("BST empty")
			return
		if data < self.key:
			if self.lchild:
				self.lchild = self.lchild.delete(data)
			else:
				print("Element not found")
				return
		elif data > self.key:
			if self.rchild:
				self.rchild = self.rchild.delete(data)
			else:
				print("Element not found")
				return


	# Traversing Techniques

	# 1. Preorder traversal
	def preorder(self):
		print(self.key, end=" ")
		if self.lchild:
			self.lchild.preorder()
		if self.rchild:
			self.rchild.preorder()

	# 2. Inorder Traversal
	def inorder(self):
		if self.lchild:
			self.lchild.inorder()
		print(self.key, end=" ")
		if self.rchild:
			self.rchild.inorder()

	# 3. Postorder Traversal
	def postorder(self):
		if self.lchild:
			self.lchild.postorder()
		if self.rchild:
			self.rchild.postorder()
		print(self.key, end=" ")

tree = BST(7)

# tree.insert(20)

for i in [8,9,10,11,12,13]:
	tree.insert(i)

print("Preorder Traversal")
tree.preorder()
print()
print("Inorder Traversal")
tree.inorder()
print()
print("Postorder Traversal")
tree.postorder()

print()
tree.search(10)



