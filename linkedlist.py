class node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = node(data,self.head)

    def insert_at_end(self, data):
        if not self.head:
            self.insert_at_beginning(data)
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = node(data)

    def get_length(self):
        counter = 0
        temp = self.head
        while(temp):
            counter += 1
            temp = temp.next
        print("Total Length: ",counter)
        return counter

    def insert_at_any_location(self,index, data):
        if not self.head or index==0:
            self.insert_at_beginning(data)
            return

        if index<0:
            if abs(index) <= self.get_length():
                index = (self.get_length() - abs(index)) + 1
            else:
                self.insert_at_beginning(data)
                return
        if index<=self.get_length():
            count = 1
            temp = self.head
            while temp:
                if count == index:
                    temp.next = node(data,temp.next)
                    return
                count +=1
                temp = temp.next
        else:
            self.insert_at_end(data)
            return

    def remove_at_begining(self):
        if not self.head:
            print("linked list is empty!!!")
            return
        self.head = self.head.next

    def remove_at_end(self):
        if not self.head:
            print("linked list is empty!!!")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def remove_at_any_location(self,index):
        if not self.head:
            print("linked list is empty!!!")
            return
        if index > 1 and index <= self.get_length():
            count = 1
            temp = self.head
            while temp:
                if count == index-1:
                    next = temp.next.next
                    #temp.next = None
                    temp.next = next
                    return
                temp = temp.next
                count += 1
        elif index == 1:
            self.remove_at_begining()
            return
        else:
            print("index not found")
            return

    def display(self):
        temp = self.head
        while temp:
            print(temp.data," -> ", end = "")
            temp = temp.next
        print()
        return

ll = linkedlist()
ll.insert_at_beginning(15)
ll.insert_at_beginning(10)
ll.insert_at_end(30)
ll.insert_at_any_location(-100, 50)
ll.display()
ll.remove_at_end()
ll.display()
ll.remove_at_begining()
ll.display()
ll.remove_at_any_location(2)
ll.display()
