class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_end(self, data):
		if not self.head:
			self.head = Node(data, self.head)
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = Node(data, next)

	def check_palindrome(self):
		slow = self.head
		fast = self.head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		prev = None
		while slow:
			n = slow.next
			slow.next = prev
			prev = slow
			slow = n
		t = self.head
		while prev:
			if prev.data != t.data:
				return False
			t = t.next
			prev = prev.next
		return True

	def folding_linked_list(self):
		slow = self.head
		fast = self.head
		count = 0
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			count += 1
		prev = None
		while slow:
			n = slow.next
			slow.next = prev
			prev = slow
			slow = n
		temp = self.head
		while count:
			n = temp.next
			p = prev.next
			temp.next = prev
			prev.next = n 
			temp = n 
			prev = p
			count -= 1

	def display(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
		print()



l = LinkedList()
l.insert_end(10)
l.insert_end(20)
l.insert_end(30)
l.insert_end(40)
l.insert_end(50)

a = l.display()
# print(l.check_palindrome())
l.folding_linked_list()
l.display()





		