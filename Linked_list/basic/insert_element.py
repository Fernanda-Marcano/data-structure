class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_element_in_position(self, element:int, position:int):
        new_node = Node(element)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current.next is not None and count < position -1:
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')


lista = LinkedList()
lista.insert_element_in_position(20, 1)
lista.print_list()