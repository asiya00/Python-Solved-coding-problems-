class Queue:
	def __init__(self, size):
		self.front = -1
		self.rear = -1
		self.size = size
		self.arr = [0]*size

	def isempty(self):
		if self.front == self.rear + 1 or self.rear == -1:
			return True
		return False

	def isfull(self):
		if self.rear == self.size - 1:
			return True
		return False

	def enqueue(self, data):
		if self.isfull():
			print("Queue is full")
			return
		self.rear += 1
		self.arr[self.rear] = data
		if self.front == -1:
			self.front += 1

	def dequeue(self):
		if self.isempty():
			print("Queue is empty")
			return
		self.front += 1

	def first_non_repeating_stream(self, s):
		characters = [0]*26
		for i in s:
			self.enqueue(i)
			characters[(ord(i) - 65)%26] += 1
			while not self.isempty():
				if characters[(ord(self.arr[self.front])-65)%26] > 1:
					self.dequeue()
				else:
					print(self.arr[self.front], end=" ")
					break
			if self.isempty():
				print(-1, end=" ")

	# def display(self):
	# 	print(self.arr[self.front:self.rear+1])

s = input()
q = Queue(len(s))
q.first_non_repeating_stream(s)
# q.first_non_repeating_stream("AAAC")
# q.display()
		