import heapq

graph = {
    'B': {'A': 25, 'C': 15},
    'C': {'B': 15, 'E': 21},
    'D': {'A': 18, 'E': 11},
    'A': {'B': 25, 'D': 18},
    'E': {'C': 21, 'D': 11, },
}
for node in graph:
    for neighbor, cost in graph[node].items():
        graph[neighbor][node] = cost

def heuristic_none(start, goal):
    return 0

def heuristic_distance(start, goal):
   return len(graph[start])  # Simple heuristic: count the number of nodes traversed

#Check if there is a direct edge between  start and goal node and returns energy cost else return 0
def heuristic_energy(start, goal):
    if goal in graph[start]:
        return graph[start][goal]
    return 0
#takes graph, start, goal and heuristic function
def a_star_search(graph, start, goal, heuristic_func):
    open_list = [(0, start, [start])]#priority queue for nodes to be explored
    g_score = {point: float('inf') for point in graph}#Cost to node
    g_score[start] = 0

    while open_list:
        _, current, path_so_far = heapq.heappop(open_list)

        if current == goal:
            yield path_so_far  # Yield the current complete path
        else:
            for neighbor in graph[current]:
                tentative_g_score = g_score[current] + graph[current][neighbor]

                if tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_list, (tentative_g_score + heuristic_func(neighbor, goal), neighbor, path_so_far + [neighbor]))

if __name__ == "__main__":
    #take user input
    start=input("Enter start state: ")
    end=input("Enter end state: ")
    
    #  (i): Find the path with the fewest stopovers
    path_task_i = list(a_star_search(graph, start, end, heuristic_none))
    print("Task (i): Find the path with the fewest stopovers")
    for path in path_task_i:
        print("Path:", path)

    #  (ii): See all paths available
    path_task_ii = list(a_star_search(graph, start, end, heuristic_none))
    print("\nTask (ii): See all paths available")
    for path in path_task_ii:
        print("Path:", path)
     # Find the cheapest path
    path_task_X = list(a_star_search(graph, start, end, heuristic_energy))
    for path in path_task_X:
        if path_task_X==path_task_ii:
            print()
        else:
         print("Path:", path)

    #  (iii): Find the cheapest path
    path_task_iii = list(a_star_search(graph, start, end, heuristic_energy))
    print("\nTask (iii): Find the cheapest path")
    for path in path_task_iii:
        print("Path:", path)

    #  (iv): Heuristics to save the battery
    path_task_iv = list(a_star_search(graph, start, end, heuristic_distance))
    print("\nTask (iv): Heuristics to save the battery")
    for path in path_task_iv:
        print("Path:", path)
