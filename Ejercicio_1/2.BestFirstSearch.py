import heapq #El módulo heapq para implementar colas de prioridad (heaps)

class Node: #definición de clase node
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state #El estado que define el nodo
        self.parent = parent #El nodo padre de donde se origina el nodo actual
        self.action = action #Action tomada desde el padre para llegar al nodo
        self.path_cost = path_cost #costo desde el nodo raiz (estado inicial), hasta el nodo actual

    def __lt__(self, other): #comparar dos objetos de clase node basado en el costo
        return self.path_cost < other.path_cost
    
def expand(problem, node):
    
    children = []

    for child in problem.actions(node.state):

        cost_action = node.path_cost + problem.action_cost(node.state, child, node)

        child = Node(child, node, None, cost_action)

        children.append(child)
    
    return children

class Problem: #DEFINICION DEL PROBLEMA
    def __init__(self, initial, goal, actions, result, action_cost, is_goal, heuristic):
        self.initial = initial #Estado inicial
        self.goal = goal #Estado objetivo
        self.actions = actions #acciones disponibles desde un estado.
        self.result = result  #estado resultante de aplicar una acción
        self.action_cost = action_cost #costo de una acción
        self.is_goal = is_goal #verificación de si el estado es el estado objetivo
        self.heuristic = heuristic #heuristica de un nodo

def best_first_search(problem, f):
    node = Node(state=problem.initial) #Crea el nodo raíz con el estado inicial del problema.
    frontier = [(f(node), node)]  # frontera como una cola de prioridad (f(n)) con el nodo inicial.
    heapq.heapify(frontier) # Convierte la lista frontier en una cola de prioridad (heap)
    reached = {problem.initial: node} #registrar los estados alcanzados y su nodo correspondiente.

    while frontier:
        _, node = heapq.heappop(frontier) #Extrae el nodo con el valor mínimo de f de la frontera.
        if problem.is_goal(node.state):   #Si el estado del nodo es el estado objetivo, devuelve el nodo.
            return node

        for child in expand(problem, node): #Expande el nodo generando sus nodos hijos.
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost: #Si el estado del nodo hijo no ha sido alcanzado antes o si se alcanza con un costo de camino menor, actualiza el dict y añade el nodo hijo a la frontera.
                reached[s] = child
                heapq.heappush(frontier, (f(child), child)) # Añade el nodo hijo a la frontera

    return None  #Se exploran todos los nodos posibles, y no se encuentra una solución solución

def result(state, action):
    return action

def action_cost(state, action, result):
    return action_costs.get((state, action), float('inf'))#En el caso de que no se encuentre un costo, el valor sera infinito

def is_goal(state):
    return state == goal

# f(n) = g(n) + h(n)
def f(node):
    return node.path_cost + problem.heuristic(node.state) #costo del camino desde el estado inicial hasta el nodo actual mas la heuristica del nodo.

initial = 'Arad'
goal = 'Bucharest'

actions = {
    # Completar con las acciones disponibles desde cada estado
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vileea'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Craiova', 'Mehadia'],
    'Craiova': ['Drobeta', 'Rimnicu Vileea', 'Pitesti'],
    'Rimnicu Vileea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Pitesti': ['Rimnicu Vileea', 'Craiova', 'Bucharest'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti']
}

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Fagaras': 176,
    'Lugoj': 244,
    'Mehadia': 241,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vileea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374
}

action_costs = {
    # Completar con los costos de las acciones
    ('Arad', 'Sibiu'): 140,
    ('Sibiu', 'Arad'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Timisoara', 'Arad'): 118,
    ('Arad', 'Zerind'): 75,
    ('Zerind', 'Arad'): 75,
    ('Zerind', 'Oradea'): 71,
    ('Oradea', 'Zerind'): 71,
    ('Timisoara', 'Lugoj'): 111,
    ('Lugoj', 'Timisoara'): 111,
    ('Oradea', 'Sibiu'): 151,
    ('Sibiu', 'Oradea'): 151,
    ('Sibiu', 'Fagaras'): 99,
    ('Fagaras', 'Sibiu'): 99,
    ('Sibiu', 'Rimnicu Vileea'): 80,
    ('Rimnicu Vileea', 'Sibiu'): 80,
    ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Lugoj'): 70,
    ('Mehadia', 'Drobeta'): 75,
    ('Drobeta', 'Mehadia'): 75,
    ('Drobeta', 'Craiova'): 120,
    ('Craiova', 'Drobeta'): 120,
    ('Rimnicu Vileea', 'Craiova'): 146,
    ('Craiova', 'Rimnicu Vileea'): 146,
    ('Craiova', 'Pitesti'): 138,
    ('Pitesti', 'Craiova'): 138,
    ('Rimnicu Vileea', 'Pitesti'): 97,
    ('Pitesti', 'Rimnicu Vileea'): 97,
    ('Pitesti', 'Bucharest'): 101,
    ('Bucharest', 'Pitesti'): 101,
    ('Fagaras', 'Bucharest'): 211,
    ('Bucharest', 'Fagaras'): 211,
}

problem = Problem(initial, goal, lambda s: actions.get(s, []), result, action_cost, is_goal, lambda s: heuristic.get(s, []))
solution = best_first_search(problem, f)#Resultado del algoritmo best_first_search aplicado al problema definido.

if solution:
    path = []
    while solution:
        path.append(solution.state)
        solution = solution.parent
    path.reverse()
    print("Solution path:", path)
else:
    print("No solution found")