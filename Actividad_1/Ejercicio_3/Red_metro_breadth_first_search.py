from collections import deque #Implementación de colas

import time
import tracemalloc

class Node: #definición de clase node
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state #El estado que define el nodo
        self.parent = parent #El nodo padre de donde se origina el nodo actual
        self.action = action #Action tomada desde el padre para llegar al nodo

    def __lt__(self, other): #comparar dos objetos de clase node basado en el costo
        return self.path_cost < other.path_cost
    
def expand(problem, node):
    s = node.state #estado actual
    for action in problem.actions(s): #pasa por todas las acciones posibles en el estado actual
        s_prime = problem.result(s, action) #Nuevo estado despues de aplicar la acción
        yield Node(state=s_prime, parent=node, action=action) #conserva el valor y pausa la ejecución de la función,
        #cuando se vuelva a invocar se reiniciará desde la declaración del yield

def result(state, action):
    return action

def is_goal(state):
    return state == goal

def breadth_first_search(problem):
    # Completar con la búsqueda en amplitud
    node = Node(state=problem.initial)
    frontier = deque([node])
    reached = {problem.initial: node}

    while frontier:
        node = frontier.popleft()

        if problem.is_goal(node.state):
            return node
        
        for child in expand(problem, node):
            s = child.state

            if s not in reached:
                reached[s] = child
                frontier.append(child)


    return None  #Se exploran todos los nodos posibles, y no se encuentra una solución solución

class Problem:
    def __init__(self, initial, goal, actions, result, is_goal):
        self.initial = initial #Estado inicial
        self.goal = goal #Estado objetivo
        self.actions = actions #acciones disponibles desde un estado.
        self.result = result  #estado resultante de aplicar una acción
        self.is_goal = is_goal #verificación de si el estado es el estado objetivo

initial = 'A'
goal = 'J'

actions = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','F'],
    'D' : ['B','G'],
    'E' : ['B','H','I'],
    'F' : ['C','J'],
    'G' : ['D'],
    'H' : ['E'],
    'I' : ['E','J'],
    'J' : ['F','I']
}

problem = Problem(initial, goal, lambda s: actions.get(s, []), result, is_goal)

tracemalloc.start()
start_time = time.time()

solution = breadth_first_search(problem)#Resultado del algoritmo breadth_first_search aplicado al problema definido.

end_time = time.time()
execution_time = end_time - start_time

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()


if solution:
    path = []
    while solution:
        path.append(solution.state)
        solution = solution.parent
    path.reverse()
    print("Solution path:", path)
else:
    print("No solution found")


print(f"Tiempo: {execution_time:.6f} s\nMemoria: {peak / 1024:.2f}KB")
