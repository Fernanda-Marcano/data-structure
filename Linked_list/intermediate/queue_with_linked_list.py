#FIFO
class Node:
    def __init__(self, data:int):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def enqueue(self, element:int):
        new_node = Node(element)
        if not self.is_empty():
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.next = None
        else:
            self.head = new_node
    
    def dequeue(self):
        if not self.is_empty():
            temp = self.head
            self.head = temp.next 
            del temp.data
    
    def front(self):
        if not self.is_empty():
            return self.head.data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        if not self.is_empty():
            count = 0
            current = self.head
            while current is not None:
                count += 1
                current = current.next
            return count
    
    def print_list(self):
        if not self.is_empty():
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')

l = LinkedList()
l.enqueue(50)
l.enqueue(60)
l.enqueue(70)
l.enqueue(80)
l.print_list()
l.dequeue()
print()
print(l.front())
l.print_list()
print(l.size())