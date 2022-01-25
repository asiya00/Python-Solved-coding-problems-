class Tree:
	def __init__(self, key, order):
		self.key = key
		self.lchild = None
		self.rchild = None
		self.order = order

	def insert(self, data, order):
		if not self.key:
			self.key = data
			return
		if data < self.key:
			if self.lchild:
				self.lchild.insert(data, 0)
			else:
				self.lchild = Tree(data, 0)
		else:
			if self.rchild:
				self.rchild.insert(data, 0)
			else:
				self.rchild = Tree(data, 0)

	def preorder(self):
	    print(self.key, end=" ")
	    if self.lchild:
	        self.lchild.preorder()
	    if self.rchild:
	        self.rchild.preorder()

	def traverse(self, n={}):
		if not self.key:
			return
		if self.lchild:
			self.lchild.traverse(n)
		if self.rchild:
			self.rchild.traverse(n)
		if not self.lchild and not self.rchild:
			self.order = 1
			if self.order in n:
				n[self.order].append(self.key)
			else:
				n[self.order] = [self.key]
		else:
			o1, o2 = 0, 0
			if self.lchild:
				o1 = self.lchild.order
			if self.rchild:
				o2 = self.rchild.order
			self.order = max(o1, o2) + 1
			if self.order in n:
				n[self.order].append(self.key)
			else:
				n[self.order] = [self.key]
		return n

	def print_nodes(self):
		nodes = self.traverse()
		# print(nodes)
		for i in nodes:
			print(*nodes[i])




t = Tree(None, 0)
t.insert(10, 0)
t.insert(9, 0)
t.insert(12, 0)
t.insert(8, 0)
t.insert(13, 0)
t.insert(67, 0)
t.insert(3, 0)
t.insert(7, 0)
t.preorder()
# t.traverse()
t.print_nodes()









