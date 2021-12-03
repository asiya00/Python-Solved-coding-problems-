class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

def makelinkedlist(list):
    head = Node(list[0])
    for i in list[1:]:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = Node(i)
    return head

def print_list(head):
    temp = head
    li = []
    while temp:
        li.append(temp.data)
        temp = temp.next
    return li

class Solution:
    def add_linkedlist(self, list1, list2):
        temp1 = list1
        temp2 = list2
        num1 = ""
        num2 = ""
        while temp1 or temp2:
            if temp1:
                num1 += str(temp1.data)
                temp1 = temp1.next
            if temp2:
                num2 += str(temp2.data)
                temp2 = temp2.next
        sumans = int(num1) + int(num2)
        sumans = list(map(int,str(sumans)))
        ans = makelinkedlist(sumans[::-1])
        return print_list(ans)

a = Solution()

list1 = makelinkedlist([3, 7, 3][::-1])
list2 = makelinkedlist([4, 5, 8][::-1])
print(a.add_linkedlist(list1, list2))
