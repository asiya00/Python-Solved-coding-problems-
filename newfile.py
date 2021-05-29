class Stack(object):
	def __init__(self):
		self.items=[]
	
	def push(self,item):
		self.items.append(item)
	
	def remove(self):
		if self.items==[]:
			print(self.items.pop())
		else:
			print("Stack is empty...")
			
	def peek(self):
		if self.items==[]:
			return self.items[-1]
		else:
			return False
	def isempty():
		if self.items==[]:
			return True
		else:
			return False
	
	def size(self):
		if self.items==[]:
			return len(self.items)
		else:
			print("Stack is empty")
			
stack=Stack()
while True:
	 	    print("Menu")
	 	    print("1. Push\n2. Pop\n3.Peek\n4.Is Empty\n5.Size\n")
	 	    ch=int(input("Enter your Choice::"))
	 	    if ch==1:
	 		     do=input("What do you like to push??")
	 		     stack.push(do)
	 	    elif ch==2:
	 		     stack.remove()
	 	    elif ch==3:
	 		     print(stack.peek())
	 	    elif ch==4:
	 		     print(stack.isempty())
	 	    elif ch==5:
	 		     print(stack.size())
	 	    else:
	 		     print("Wrong Choice....")