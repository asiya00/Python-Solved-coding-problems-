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
		middle = slow
		count = 0
		if not self.head.next:
			return
		while fast and fast.next:
			count += 1
			middle = slow
			slow = slow.next
			fast = fast.next.next
		curr = slow
		prev = None
		while curr:
			n = curr.next
			curr.next = prev
			prev = curr
			curr = n
		middle.next = None
		curr = self.head
		while prev:
			n = curr.next
			curr.next = prev
			curr = prev 
			prev = n

	def display(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
		print()



l = LinkedList()
l.insert_end(1)
l.insert_end(2)
l.insert_end(3)
l.insert_end(4)
l.insert_end(5)
l.insert_end(60)
l.insert_end(70)

a = l.display()
# print(l.check_palindrome())
l.folding_linked_list()
l.display()





		