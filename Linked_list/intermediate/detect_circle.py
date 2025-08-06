class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_last(self, element:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        else:
            self.head = new_node
            new_node.next = self.head
    
    def delete_last(self):
        if self.head is not None:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            del temp
    
    def has_circle(self):
        if self.head is not None:
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True     #Hay un ciclo. 
            return False            #No hay ciclo, fast llega hasta None
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current.next != self.head:
                print(current.data, end=' -> ')
                current = current.next
            print(current.data)

l = LinkedList()
l.insert_last(10)
l.insert_last(20)
l.insert_last(30)
l.insert_last(40)
l.insert_last(50)
l.insert_last(20)
l.insert_last(60)

l.print_list()
print()
print(l.has_circle())