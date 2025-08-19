import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from basic_structure.search_element import LinkedList
from basic_structure.simple_linked_list import SimpleLinkedList


class Node:
    def __init__(self, data:int):
        self.data = data 
        self.next = None

class LinkedListM:
    def __init__(self):
        self.head = None
    
    def insert_firts(self, element:int):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def merge_sorted_list(self, list1, list2):
        dummy = Node(0) #Nodo dummy 
        tail = dummy
        
        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')

list1 = LinkedList()
list1.insert_to_last(10)
list1.insert_to_last(30)
list1.insert_to_last(50)
list1.print_list()

list2 = SimpleLinkedList()
list2.insert_to_last(20)
list2.insert_to_last(40)
list2.insert_to_last(60)
list2.insert_to_last(80)
list2.print_list()

list3 = LinkedListM()
print(list3.merge_sorted_list(list1, list2))