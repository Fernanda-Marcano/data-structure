class Node:
    def __init__(self, data:int):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_to_last(self, element:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            previous = None
            while current is not None:
                previous = current
                current = current.next
            previous.next = new_node
            new_node.next = None
        else:
            self.head = new_node
    
    def delete_element_in_position(self, position:int):
        if self.head is not None:
            temp = self.head
            count = 1
            previous = None
            while temp.next is not None and count < position:
                previous = temp
                temp = temp.next
                count += 1
            if position == 1:
                self.head = temp.next
                del temp
            previous.next = temp.next
            del temp
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')

lista = LinkedList()
lista.insert_to_last(10)
lista.insert_to_last(20)
lista.insert_to_last(30)
lista.insert_to_last(40)
lista.insert_to_last(50)
lista.print_list()
print()
lista.delete_element_in_position(4)
lista.print_list()