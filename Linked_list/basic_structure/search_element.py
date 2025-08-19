class Node:
    def __init__(self, data:int):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_to_last(self, element:int):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            prev = None
            while current is not None:
                prev = current
                current = current.next
            prev.next = new_node
    
    def deleted_to_last(self):
        if self.head is not None:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = temp.next   #None
            del temp
    
    def lenght_list(self):
        if self.head is not None:
            count = 0
            current = self.head
            while current is not None:
                count += 1
                current = current.next
            print(f'The lenght of list is: {count}')
    
    def search_element(self, element:int):
        if self.head is not None:
            current = self.head
            while current is not None:
                if current.data == element:
                    return True
                current = current.next
            else:
                return False
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')

if __name__ == '__main__':
    list = LinkedList()
    list.insert_to_last(20)
    list.insert_to_last(30)
    list.insert_to_last(40)
    list.insert_to_last(50)
    list.lenght_list()
    list.print_list()
    print()
    print(list.search_element(30))