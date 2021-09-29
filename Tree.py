class Tree_Node:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None

	def add_node(self, child):
		child.parent = self
		self.children.append(child)

	def level(self):
		counter = 0
		p = self.parent
		while p:
			counter += 1
			p = p.parent
		return counter

	def display(self):
		print("|__" * self.level() + self.data)
		for child in self.children:
			child.display()


root = Tree_Node("home")

child1 = Tree_Node("Anaconda")
child2 = Tree_Node("Python")

root.add_node(child1)
root.add_node(child2)

subchild1 = Tree_Node("Anaconda2")
subchild2 = Tree_Node("Python3")

child1.add_node(subchild1)
child2.add_node(subchild2)

root.display()







