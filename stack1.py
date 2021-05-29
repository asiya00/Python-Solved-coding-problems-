class Stack():
	def __init__(self):
		self.items=[]
		
	def push(self,item):
		self.items.append(item)
		
	def remove(self):
		if self.items:
			self.items.pop()
		else:
			print("Stack is empty")	
	def peek(self):
		if self.items:
			return self.items[-1]
		else:
			return False
	def isempty(self):
		if self.items:
			return False
		else:
			return True
	
	def size(self):
		if self.items:
			return len(self.items)
		else:
			print("Stack is empty")
			
	def main(self):
		while True:
	 	    print("Menu")
	 	    print("1. Push\n2. Pop\n3.Peek\n4.Is Empty\n5.Size\n")
	 	    ch=int(input("Enter your Choice::"))
	 	    if ch==1:
	 		     do=input("What would you like to push??")
	 		     self.push(do)
	 	    elif ch==2:
	 	    	self.remove()
	 	    elif ch==3:
	 		     print(self.peek())
	 	    elif ch==4:
	 		     print(self.isempty())
	 	    elif ch==5:
	 		     print(self.size())
	 	    else:
	 		     print("Wrong Choice....")
	 
if __name__=="__main__":
	Stack().main()
	
	