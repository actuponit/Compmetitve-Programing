class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            return self.addAtHead(val)
        
        curr = self.head
        
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        curr = Node(0, self.head)
        if index == 0:
            return self.addAtHead(val)
            
        i = 0
        while i < index:
            curr = curr.next 
            i += 1
        curr.next = Node(val, curr.next)
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        curr = Node(0, self.head)

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        i = 0
        while i < index:
            curr = curr.next 
            i += 1
        temp = curr.next
        curr.next = temp.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)