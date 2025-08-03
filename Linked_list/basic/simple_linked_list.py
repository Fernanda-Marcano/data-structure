class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_to_first(self, element:int):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def insert_to_last(self, element:int):
        new_node = Node(element)
        if self.head is not None:
            last = self.head
            prev = None
            while last is not None:
                prev = last
                last = last.next
            prev.next = new_node
        else:
            self.head = new_node
    
    def deleted_to_firts(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            del temp
    
    def deleted_to_last(self):
        if self.head is not None:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None
            del temp
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print("None")


list = SimpleLinkedList()

list.insert_to_first(20)
list.insert_to_first(30)
list.insert_to_first(40)
list.insert_to_first(50)
list.print_list()
print()
list.insert_to_last(60)
list.insert_to_last(70)
list.print_list()

list.deleted_to_firts()
print()
list.print_list()

list.deleted_to_last()
print()
list.print_list()
