import math

N=4
inf = math.inf

def printClosure(reach):
    print ("Following matrix is the transitive closure of the given graph ")
    for i in range(N):
        for j in range(N):
            print(reach[i][j], end=" ")
        print("")

    print("")
        
def transitiveClosure(adjMatrix):

    reach = [[0 for i in range(N)] for j in range(N)]
    
    for i in range(N):
        for j in range(N):
            if adjMatrix[i][j] > 0 and adjMatrix[i][j] != inf:
                reach[i][j] = 1
       
    for k in range(N):
        for i in range(N):
            for j in range(N):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
                
    printClosure(reach) 

def printPath(path, v, u):
    if (path[v][u] == v):
        return
    printPath(path, v, path[v][u])
    print(path[v][u], end=" ")

def printSolution(cost, path):
    print("Shortest Distance between every pair of nodes: ")
    for v in range(N):
        print(cost[v])
    
    for v in range(N):
        for u in range(N):
            if(u != v and path[v][u] != -1):
                print("\nShortest Path from vertex", v,"to vertex", u,"is:",v," ", end="")
                printPath(path, v, u)
                print(u)
                print("The distance covered in this path is:", cost[v][u])

def FloydWarshall(adjMatrix):
    cost = [[0 for col in range(N)] for row in range(N)]
    path = [[0 for col in range(N)] for row in range(N)]
    
    for v in range(N):
        for u in range(N):
            cost[v][u] = adjMatrix[v][u]
            
            if (v == u):
                path[v][u] = 0
            elif(cost[v][u] != inf):
                path[v][u] = v
            else:
                path[v][u] = -1
                
    for k in range(N):
        for v in range(N):
            for u in range(N):
                if (cost[v][k] != inf and cost[k][u] != inf and cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]
            
            if (cost[v][v] < 0):
                print("Negative Weight Cycle Found!!")
                return
            
    printSolution(cost, path)
    
#Driver Code
    
# Here, the adjacency matrix is the distance matrix itself
adjMatrix = [[0, 10, 2, 1], [inf, 0, 3, inf], [inf, inf, 0, 20], [inf, 1, inf, 0]]

transitiveClosure(adjMatrix)

FloydWarshall(adjMatrix)
