# Swap kth elements from both side


class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		self.head = Node(data, self.head)

	def get_count(self):
		counter = 0
		temp = self.head
		while temp:
			counter += 1
			temp = temp.next
		return counter

	def swap(self, k):
		n = self.get_count()
		count = 0

		if n < k:
			return
		if (2*k-1) == n:
			return

		x = self.head
		x_prev = x

		for i in range(k-1):
			x_prev = x
			x = x.next

		y = self.head
		y_prev = y

		for j in range(n-k):
			y_prev = y
			y = y.next

		if x_prev != None:
			x_prev.next = y 
		if y_prev != None:
			y_prev.next = x

		temp = x.next
		x.next = y.next
		y.next = temp

		if k == 1:
			self.head = y

		if k == n:
			self.head = x

	def display(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

l = LinkedList()
l.insert(4)
l.insert(3)
l.insert(2)
l.insert(1)
l.display()
l.swap(2)
l.display()
