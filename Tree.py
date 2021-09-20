class Tree_Node:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None

	def add_node(self, child):
		child.parent = self
		self.children.append(child)

	def display(self):
		print(self.data)
		for child in self.children:
			print(child.data)


root = Tree_Node("home")

child1 = Tree_Node("Anaconda")
child2 = Tree_Node("Python")

root.add_node(child1)
root.add_node(child2)

root.display()
