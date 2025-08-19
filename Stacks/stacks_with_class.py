#Implementar una pila usando clases 

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, element:int) -> int:
        self.items.append(element)
    
    def pop(self) -> int:
        if not self.is_empty():
            return self.items.pop()
        raise IndexError('Pop from empty stack')
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def peek(self) -> int:
        if not self.is_empty():
            return self.items[-1]
        raise IndexError('Peek from empty stack')
    
    def size(self) -> int:
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items[::-1])

pila = Stack()
print(pila)

pila.push(20)
pila.push(30)
pila.push(40)

print(pila)
print(f'Peek -> {pila.peek()}')