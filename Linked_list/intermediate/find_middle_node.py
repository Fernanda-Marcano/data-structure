class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_to_firts(self, element:int):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def insert_to_last(self, element:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.next = None
        else:
            self.head = new_node
    
    #fast and slow pointers
    def find_middle(self):
        if self.head is not None:
            slow = self.head
            fast = self.head
            while fast and fast.next: #Mientras fast no llegue al final
                slow = slow.next        #1 Paso
                fast = fast.next.next   #2 Pasos
            return slow.data
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')


l = LinkedList()
l.insert_to_last(10)
l.insert_to_last(20)
l.insert_to_last(30)
l.insert_to_last(40)
l.insert_to_last(50)
l.insert_to_last(60)
l.print_list()
print()
print(l.find_middle())