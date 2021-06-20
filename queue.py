class Queue:
	def __init__(self,size):
		self.size = size
		self.elements = [None]*size
		self.front = -1
		self.rear = -1

	def isempty(self):
		if self.front == self.rear+1 or self.rear == -1:
			return True
		return False

	def isfull(self):
		if self.rear == self.size-1:
			return True
		return False

	def enqueue(self, data):
		if self.isfull():
			print("Queue is full")
			return
		self.rear += 1
		self.elements[self.rear] = data

	def dequeue(self):
		if self.isempty():
			print("Queue is empty")
			return
		self.front+=1
		p = self.elements[self.front]
		return p

	def display(self):
		return self.elements[self.front+1:self.rear+1]

q = Queue(5)

print(q.display())
print(q.dequeue())
print(q.dequeue())
q.enqueue(21)
print(q.dequeue())
print(q.display())
