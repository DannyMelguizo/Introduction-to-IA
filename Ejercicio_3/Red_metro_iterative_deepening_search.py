from collections import deque

import time
import tracemalloc

class Node:
    def __init__(self, state, parent=None, action=None, depth=0): #Definición de la clase Node
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def __repr__(self): #Definición de los print asociados en la clase para hacer seguimiento de estados de node
        return f"Node({self.state})"

def depth_limited_search(problem, limit):
    frontier = deque([Node(problem.initial)])  # creación de frontera LIFO queue
    result = 'failure' #Inicialización de variable result

    while frontier:
        node = frontier.pop()

        if problem.is_goal(node.state):
            return node

        if node.depth > limit: #corte de arbol si no se cumple con el limite definido
            result = 'cutoff'  #valido solo en implementaciones de interactive deepening
        else:
            for child in expand(problem, node):
                if not is_cycle(child):  #verificación de ciclos redundantes
                    frontier.append(child)

    return result

def iterative_deepening_search(problem): #Implementación de iterative_deepening
    for depth in range(9):  # limite definido a partir de la ddefinición del problema
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':  #casos de corte
            return result
    return None

def expand(problem, node):
    children = []
    for action in problem.actions(node.state):
        child_state = problem.result(node.state, action)
        child_node = Node(child_state, parent=node, action=action, depth=node.depth + 1) #aumentar la profuncidad en 1 unidad para hacer tracking
        children.append(child_node)
    return children

def result(state, action):
    return action

def is_goal(state):
    return state == goal

def is_cycle(node): #Verificación de ciclos redundantes (Evitar llegar a a ciclos infinitos)
    current = node.parent
    while current is not None:
        if current.state == node.state:
            return True
        current = current.parent
    return False

class Problem:
    def __init__(self, initial, goal, actions, result, is_goal):
        self.initial = initial
        self.goal = goal
        self.actions = actions
        self.result = result
        self.is_goal = is_goal

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

# Ejecución del problema
problem = Problem(initial, goal, lambda s: actions.get(s, []), result, is_goal)

tracemalloc.start()
start_time = time.time()

solution = iterative_deepening_search(problem)

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