class Node:
	def __init__(self,data, next=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.h = None

	def insert_at_first(self, data):
		self.h = Node(data, self.h)

	def insert_at_end(self, data):
		if not self.h:
			self.insert_at_first(data)
		else:
			temp = self.h 
			while(temp.next):
				temp = temp.next

			temp.next = Node(data, next)

	def get_length(self):
		temp = self.h
		counter = 0
		while temp:
			counter += 1
			temp = temp.next
		return counter

	def insert_at_index(self, index, data):
		if not self.h or index == 0 or index == 1:
			self.insert_at_first(data)
			return

		if index<0:
			if abs(index) <= self.get_length():
				index = self.get_length() + index + 1
			else:
				self.insert_at_first(data)
				return

		if index < self.get_length():
			count = 1
			temp = self.h
			while temp:
				if count == index:
					p = Node(data, next)
					p.next = temp.next
					temp.next = p
					return
				count +=1
				temp = temp.next
		else:
			self.insert_at_end(data)
			return

	def remove_end(self):
		if not self.h:
			print("Empty Linked List")
			return 
		temp = self.h
		while temp.next.next:
			temp = temp.next

		temp.next = None

	def remove_at_first(self):
		if not self.h:
			print("Linked List Empty")
			return
		self.h = self.h.next

	def remove_at_index(self, index):
		if not self.h:
			print("Linked List is empty")
			return
		if index==1:
			self.remove_at_first()
		if index <= self.get_length():
			count = 1
			temp = self.h
			while temp:
				if count == index:
					temp.next = temp.next.next
					return
				count += 1
				temp = temp.next


	def display(self):
		temp = self.h 
		while(temp):
			print(temp.data,end=" ")
			temp = temp.next
		print()


li = LinkedList()

li.insert_at_first(10)
li.insert_at_end(20)
li.insert_at_end(50)
li.insert_at_end(60)
li.insert_at_end(70)
li.insert_at_end(80)
li.insert_at_end(15)
li.display()
li.insert_at_index(2,30)
li.display()
li.insert_at_index(-2,40)
li.display()
li.display()
li.remove_end()
li.display()
li.remove_at_first()
li.display()
li.remove_at_index(3)
li.display()



