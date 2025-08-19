class Node:
    def __init__(self, data:int):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, element:int):
        new_node = Node(element)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insert_last(self, element:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        else:
            self.head = new_node
    
    def insert_in_position(self, element:int, position:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            count = 0
            while current.next is not None and count < position-1:
                count += 1
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if new_node.next is not None:
                new_node.next.prev = new_node
            current.next = new_node
    
    def delete_first(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            temp.next.prev = self.head
            del temp
    
    def delete_last(self):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = temp.next
            del temp
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')


l = DoubleLinkedList()
l.insert_first(90)
l.insert_first(50)
l.insert_first(30)
l.print_list()

l.insert_last(100)
l.insert_last(40)
l.insert_last(80)
l.print_list()

l.delete_last()
l.print_list()

l.delete_first()
l.print_list()

print()
l.insert_in_position(20, 3)
l.print_list()