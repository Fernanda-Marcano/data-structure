#Implementacion de pila (stack) usando listas de python (La forma mas simple)

stack = []

#push 
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print(f'Elementos de la pila {stack}')

#peek / front
peek = stack[-1]
print(f'Elemento tope de la pila -> {peek}')

#pop
top = stack.pop()
print(f'Elemento desapilado: {top}')
print(f'Elementos de la pila {stack}')

is_empty = len(stack) == 0 
print(f'Esta vacia?: {is_empty}')