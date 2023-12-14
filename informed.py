import operator
class environment(object):
    my_graph = {
    "A":set(["B","D"]),
    "B":set(["A","C"]),
    "C":set(["B","E"]),
    "E":set(["C","D"]),
    "D":set(["A","E"]),
    "6":set(["3","5","9"]),
    "7":set(["4","8"]),
    "8":set(["5","7","9"]),
    "9":set(["6","8"]) 
    }
    state = "B" #str(input("enter your start point: "))
    goal = "E" #str(input("enter your end point: "))
    
    cost = {str(["A","B"]): "3", str(["1","4"]): "5", 
    str(["2","1"]):"3", str(["2","3"]):"5", str(["2","5"]):"7",
    str(["3","2"]):"5", str(["3","6"]):"9",
    str(["4","1"]):"5", str(["4","5"]):"9", str(["4","7"]):"11",
    str(["5","2"]):"7", str(["5","4"]):"9", 
    str(["5","8"]):"13",str(["5","6"]):"11",
    str(["6","3"]):"9", str(["6","5"]):"11", str(["6","9"]):"15",
    str(["7","4"]):"11", str(["7","8"]):"15",
    str(["8","5"]):"13", str(["8","7"]):"15", str(["8","9"]):"17",
    str(["9","6"]):"15", str(["9","8"]):"17" 
    }
    
    myhristics = {"1":["1","3"],
    "2":["2","3"],
    "3":["3","3"],
    "4":["1","2"],
    "5":["2","2"],
    "6":["3","2"],
    "7":["1","1"],
    "8":["2","1"],
    "9":["3","1"]
    }
    #ask the user to enter their current status
    #randomly select the initial state
 
class agent(environment):
    def get_h(vertex, goal):
        v = [] 
        g = []
        for i in environment.myhristics[vertex]:
            v.append(int(i))
        for i in environment.myhristics[goal]:
            g.append(int(i))
        h = abs(v[0] - g[0]) + abs(v[1] - g[1])
        return h
   # def gbfs (graph, start, goal):
    #    p = []
     #   p.append(start)
      #  while True:
       #     neighbour = graph[start]
        #    h = {}
         #   for i in neighbour.difference(p):
          #      h[i] = agent.get_h(i,goal)
 #
  #          sorted_h = sorted(h.items(),key = operator.itemgetter(1))
   #         x = next(iter(sorted_h[0]))
    #        p.append(x)
     #       if x == goal:
      #       return p
       #     else:
        #        start = x
    def astar (graph, start, goal):
        p = []
        p.append(start)
        while True:
            neighbour = graph[start]
            h = {}
            for i in neighbour.difference(p):
              l = []
            l.append(str(start))
            l.append(str(i))
            h[i] = agent.get_h(i,goal) + agent.get_cost(l)
            sorted_h = sorted(h.items(),key = operator.itemgetter(1))
            x = next(iter(sorted_h[0]))
            p.append(x)
            if x == goal:
             return p
            else:
             start = x 
    def get_cost(path_to_cost):
 
        i = 0
        path_cost = 0
        while i < len(path_to_cost)-1:
            l = []
            l.append(path_to_cost[i])
            l.append(path_to_cost[i+1])
            path_cost = path_cost+int(environment.cost[str(l)])
            i +=1
        return path_cost
    def __init__(self, environment):
#        print("gbfs heuristic path", agent.gbfs(environment.my_graph, 
#        environment.state, environment.goal)) 
        print("astar heuristic and cost path",
        agent.astar(environment.my_graph, 
        environment.state,environment.goal)) 
 
envt = environment
agent1 = agent(envt)
