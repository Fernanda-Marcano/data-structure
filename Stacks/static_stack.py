class StaticStack:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1   #Indice del tope, -1 significa vacia
    
    def push(self, item:int):
        #Añade un elemento al tope de la pila
        if self.is_full():
            raise OverflowError('The stack is full')
        self.top += 1
        self.stack[self.top] = item
    
    def pop(self):
        #Elimina y devuelve el elemento del tope
        if self.is_empty():
            raise IndexError('The stack is null')
        item = self.stack[self.top]
        self.stack[self.top] = None #Opcional: limpiar referencia
        self.top -= 1
        return item
    
    def peek(self):
        """Muestra el elemento del tope sin eliminarlo"""
        if self.is_empty():
            raise IndexError('La pila esta vacia')
        return self.stack[self.top]
    
    def is_empty(self):
        #Verifica si la pila esta vacia 
        return self.top == -1
    
    def is_full(self):
        #Verifica si la pila esta llena
        return self.top == self.capacity - 1
    
    def size(self):
        #Devuelve el numero de elementos actuales
        return self.top + 1
    
    def __str__(self):
        elements = [str(self.stack[i]) for i in range(self.top + 1)]
        return '['+ ', '.join(reversed(elements)) + '] (Tope)'

s_stack = StaticStack(3)
s_stack.push(10)
s_stack.push(20)
print(s_stack)
s_stack.push(30)
print(f'Llena? {s_stack.is_full()}')
print(s_stack)
print(s_stack.pop())
print(s_stack)
print(s_stack.size())