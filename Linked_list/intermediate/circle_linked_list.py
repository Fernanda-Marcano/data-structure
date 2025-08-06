#Circle Linked List

class Node:
    def __init__(self, data:int):
        self.data = data 
        self.next = None


class CircleLinkedList:
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
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            del temp.data
    
    def has_circle(self):
        if self.head is not None:
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current.next != self.head:
                print(current.data, end=' -> ')
                current = current.next
            print(current.data)


c_list = CircleLinkedList()

for i in range(10, 60, 10):
    c_list.insert_last(i)

c_list.print_list()

c_list.delete_last()

c_list.print_list()

print(c_list.has_circle())