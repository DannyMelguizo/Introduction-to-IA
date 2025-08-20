## 1. Problema
Encontrar la ruta optima de un punto A `Arad` a un punto B `Bucharest`. Teniendo en cuenta que ir de una ciudad a otra tiene un costo y cada ciudad maneja una heuristica (unidad adicional que ayuda a determinar a que distancia esta el objetivo).

## 2. Algoritmo
Se utiliza el Algoritmo A* en el cual tenemos tanto el costo como la heuristica para la toma de decisiones de que ciudad sera la siguiente a evaluar.

```python
def best_first_search(problem, f):
    node = Node(state=problem.initial) #Crea el nodo raíz con el estado inicial del problema.
    frontier = [(f(node), node)]  # frontera como una cola de prioridad (f(n)) con el nodo inicial.
    heapq.heapify(frontier) # Convierte la lista frontier en una cola de prioridad (heap)
    reached = {problem.initial: node}

    while frontier:
        _, node = heapq.heappop(frontier) #Extrae el nodo con el valor mínimo de f de la frontera.
        if problem.is_goal(node.state):   
            return node

        for child in expand(problem, node): 
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                heapq.heappush(frontier, (f(child), child)) # Añade el nodo hijo a la frontera

# f(n) = g(n) + h(n)
def f(node):
    return node.path_cost + problem.heuristic(node.state) #costo del camino desde el estado inicial hasta el nodo actual mas la heuristica del nodo.
```