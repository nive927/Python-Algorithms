from itertools import permutations

def h_circuit(n, adj):
    for s in permutations(range(1, n)):
        if (goalTest(s, adj)):
            yield s

def goalTest(s, adj):
    
    if (not adj[0][s[0]]):
        return False
    for i in range(len(s) - 1):
        if ( not adj[s[i]][s[i+1]] ):
            return False
    return adj[s[len(s) - 1]][0] == 1

def vertexAdd(v, path, adj):
    return (adj[path[len(path) - 1]][v] and v not in path)

def h_backtrack(adj, num, path):
    
    if (num == n and adj[path[num - 1]][0]):
        print(path + [0])
               
    for i in range(n):
        if( vertexAdd(i, path, adj) ):
            path.append(i)
            h_backtrack(adj, num+1, path)
            path.pop()

#Driver 
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

#Space separated edges with one edge on each line
print("\nEnter Edges: ")

adj = [[0]*n for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    adj[a][b] = 1
    adj[b][a] = 1
    
print("\nThe adjacency matrix:")
for i in range(n):
    print(adj[i])
            
print("\nList of all hamiltonian cycles:")
for tup in h_circuit(n, adj):
    print((0,) + tup + (0,))
 
print("\nList of all hamiltonian cycles from backtracking:")           
h_backtrack(adj, 1, [0])