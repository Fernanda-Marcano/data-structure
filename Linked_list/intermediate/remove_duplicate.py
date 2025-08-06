class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_last(self, element:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.next = None
        else:
            self.head = new_node
    
    def delete_last(self):
        if self.head is not None:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            del temp
    
    def remove_duplicates(self):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                if temp.data == temp.next.data:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end='None')
                current = current.next
            print('None')