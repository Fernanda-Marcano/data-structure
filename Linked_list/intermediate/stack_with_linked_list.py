#LIFO

class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, element:int):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if not self.is_empty():
            temp = self.head
            self.head = temp.next
            del temp
    
    def is_empty(self):
        return self.head is None
    
    def peek(self):
        if not self.is_empty():
            return self.head.data
    
    def size(self):
        if not self.is_empty():
            count = 0
            current = self.head
            while current is not None:
                count += 1
                current = current.next
            return count
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')

l = LinkedList()
l.push(10)
l.push(20)
l.push(30)
l.push(40)
l.push(50)
l.push(60)
l.print_list()
print()
print(l.peek())
print()
l.pop()
print(l.peek())
l.print_list()
print()
print(f'Size: {l.size()}')