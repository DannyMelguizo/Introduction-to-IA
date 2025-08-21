import heapq #El módulo heapq implementa colas de prioridad (heaps)

class Node:
    def __init__(self, position, parent=None, path_cost=0, action=None): #AGREGAR ACTION
        self.position = position
        self.parent = parent
        self.path_cost = path_cost
        self.action = action

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Problem:
    def __init__(self, start, goal, actions):
        self.start = start
        self.goal = goal
        self.actions = actions

def find_exit(maze):

    #DEFINA el conjunto de actions posibles#
    actions = {
        (-1,0): 'Up',
        (1,0): 'Down',
        (0,-1): 'Left',
        (0,1): 'Right'
    }

    problem=Problem(start, goal, actions)#COMPLETE LA DEFINICIÓN DEL OBJETO Y ADAPTELO EN LOS PUNTOS QUE LO REQUIERAN

    def manhatan_distance(pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])  # Distancia de Manhattan

    def get_neighbors(pos):  #ESTA ES LA FUNCIÓN QUE DEBERIA AJUSTAR PARA HACER TRACKING DE LOS MOVIMIENTOS (Up, Down, Right, Left)
        neighbors = [] #lista de vecinos
        for move in [x for x in problem.actions.keys()]:  #Tenga en cuenta que para que esto sea funcional ya debio haber definido el objeto problem
            neighbor = (pos[0] + move[0], pos[1] + move[1])
            if maze[neighbor[0]][neighbor[1]] != "#": #si el vecino es diferente a "#" pared agregarlo a la lista de vecinos                neighbors.append(neighbor)
              neighbors.append(neighbor)
        return neighbors

    start_node = Node(start, path_cost=0)
    frontier = [(manhatan_distance(start, goal), start_node)]
    heapq.heapify(frontier) #Convierte la lista frontier en una cola de prioridad (heap)
    reached = {start: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)
        if node.position == goal:
            return reconstruct_path(node)

        for neighbor in get_neighbors(node.position):
            new_cost = node.path_cost + 1
            if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                action_made = problem.actions[(neighbor[0] - node.position[0], neighbor[1] - node.position[1])]
                reached[neighbor] = Node(neighbor, parent=node, path_cost=new_cost, action=action_made)
                heapq.heappush(frontier, (manhatan_distance(neighbor, goal), reached[neighbor]))

    return None  # No se encontró salida

def reconstruct_path(node):  #AJUSTAR FUNCIONES PARA ADEMAS DE LAS POSICIONES, MOSTRAR LAS ACCIONES TOMADAS
    path = []
    while node:
        path.append((node.position, node.action))
        node = node.parent
    path.reverse()
    return path


start = (1, 1)  # Posición inicial basado en la documentación suministrada
goal = (1, 6)    # Posición de la salida basado en la documentación suministrada

maze = [
    ["#", "#", "#", "#", "#", "#", "#","#"],
    ["#", "S", "#", " ", "#", " ", "E","#"],
    ["#", " ", " ", " ", "#", " ", " ","#"],
    ["#", " ", "#", " ", " ", " ", "#","#"],
    ["#", "#", "#", "#", "#", "#", "#","#"],
    ["#", "#", "#", "#", "#", "#", "#","#"]
]
path = find_exit(maze)
print("Path to exit:", path)