class BST:
	def __init__(self, key):
		self.key = key
		self.lchild = None
		self.rchild = None

	# Insert method
	def insert(self, data):
		if self.key is None:
			self.key = data
			return
		if data < self.key:
			if self.lchild:
				self.lchild.insert(data)
			else:
				self.lchild = BST(data)
		else:
			if self.rchild:
				self.rchild.insert(data)
			else:
				self.rchild = BST(data)

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

	# Minimum element
	def getmin_ele(self):
		current = self.lchild
		if not current:
			return self.key
		while current.lchild:
			current = current.lchild
		return current.key

	# Maximum element
	def getmax_ele(self):
		current = self.rchild
		if not current:
			return self.key
		while current.rchild:
			current = current.rchild
		return current.key


	# Delete method
	def delete(self, data, curr):
		if not self.key:
			print("BST empty")
			return
		if data < self.key:
			if self.lchild:
				self.lchild = self.lchild.delete(data, curr)
			else:
				print("Element not found")
				return
		elif data > self.key:
			if self.rchild:
				self.rchild = self.rchild.delete(data, curr)
			else:
				print("Element not found")
				return			
		else:
			if self.lchild is None:
				temp = self.rchild
				if data == curr:
					self.key = temp.key
					self.lchild = temp.lchild
					self.rchild = temp.rchild
					temp = None
					return
				self = None
				return temp
			elif self.rchild is None:
				temp = self.lchild
				if data == curr:
					self.key = temp.key
					self.lchild = temp.lchild
					self.rchild = temp.rchild
					temp = None
					return
				self = None
				return temp
			else:
				node = self.rchild
				while node.lchild:
					node = node.lchild				
				self.key = node.key
				self.rchild = self.rchild.delete(node.key, curr)
		return self
					

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

def count(node):
	if node is None:
		return 0
	return 1 + count(node.lchild) + count(node.rchild)

tree = BST(None)

# tree.insert(20)

for i in [10, 7, 8, 9, 11, 2]:
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

if count(tree)>1:
	tree.delete(10, tree.key)
else:
	print("Delete operation can't be performed")
tree.preorder()
print("\nMinimum Element",tree.getmin_ele())
print("\nMaximum Element",tree.getmax_ele())