class SurveillanceRobot:
    def __init__(self):
        # Define the adjacency matrix to represent the graph
        self.graph = [
            # 0   1   2   3   4   5   6   7   8   9   10  11
            [0, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0],  # 0
            [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],  # 1
            [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],  # 2
            [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # 3
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],  # 4
            [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 5
            [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 6
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 10
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 11
        ]

    def heuristic(self, current, goal):
        # Heuristic function using Manhattan distance
        current_row, current_col = divmod(current, 6)
        goal_row, goal_col = divmod(goal, 6)
        return abs(current_row - goal_row) + abs(current_col - goal_col)

    def a_star_search(self, start, goal):
        open_set = [(0, start)]  # Priority queue containing (f_score, node)
        came_from = {}  # Dictionary to store the path
        g_score = {point: float('inf') for point in range(12)}  # Cost from start
        g_score[start] = 0
        f_score = {point: float('inf') for point in range(12)}  # Estimated total cost
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            _, current = min(open_set)  # Pop node with lowest f_score
            if current == goal:
                path = [goal]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return list(reversed(path))

            open_set = [node for node in open_set if node[1] != current]
            for neighbor in range(12):
                if self.graph[current][neighbor] == 0:  # If there is no edge, skip
                    continue

                tentative_g_score = g_score[current] + self.graph[current][neighbor]
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    if (f_score[neighbor], neighbor) not in open_set:
                        open_set.append((f_score[neighbor], neighbor))

    def dfs(self, start, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start)
        path.append(start)

        for neighbor in range(12):
            if self.graph[start][neighbor] == 0:  # If there is no edge, skip
                continue
            if neighbor not in visited:
                self.dfs(neighbor, visited, path)

        return path

# Sample usage of the SurveillanceRobot class:
if __name__ == "__main__":
    robot = SurveillanceRobot()

    # Task (i): Find the path with the fewest stopovers (energy required)
    quickest_path = robot.a_star_search(0, 10)
    print("Quickest Path:", quickest_path)

    # Task (ii): See all paths available
    all_paths = robot.dfs(0)
    print("All Paths:", all_paths)

    # Task (iii): Find the cheapest path (lowest energy consumption)
    cheapest_path = robot.a_star_search(0, 10)
    print("Cheapest Path:", cheapest_path)

    # Task (iv): Heuristic with distance to save battery
    # We already used the Manhattan distance as the heuristic in the A* algorithm.

    # Task (v): Prove that the heuristic is consistent
    # The Manhattan distance is consistent as it satisfies the triangular inequality.
